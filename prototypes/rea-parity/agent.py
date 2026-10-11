"""Parity Medic feasibility spike: real model repairs a narrow adapter against a shipped app.

The model receives source readback and training counterexamples through allowlisted tools.
Only generated adapter code is executed, in QuickJS with no host I/O bindings.
"""
import argparse
import json
import os
import subprocess
import time
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

import neatlogs
from dotenv import load_dotenv
from opentelemetry.trace import Status, StatusCode

ROOT = Path(__file__).resolve().parents[2]
NODE = ROOT / '.local/tools/node_modules/node/bin/node'
PROBE = Path(__file__).with_name('parity.mjs')
OUT = ROOT / 'docs/rea-research/evidence'
MODEL = 'deepseek-flash'


def probe(mode, data=None, name=None):
    args = [str(NODE), str(PROBE), mode] + ([name] if name else [])
    # Child never inherits API credentials. No model-provided arguments, paths or commands.
    p = subprocess.run(args, input=json.dumps(data) if data is not None else None,
                       text=True, capture_output=True, cwd=ROOT,
                       env={'PATH': str(NODE.parent) + ':/usr/bin:/bin'}, timeout=210)
    if p.returncode:
        raise RuntimeError('App probe failed: ' + p.stderr[-1200:])
    return json.loads(p.stdout) if mode != '--self-check' else p.stdout


def tool(name, description, properties):
    return {'type': 'function', 'function': {'name': name, 'description': description,
            'parameters': {'type': 'object', 'properties': properties,
                           'required': list(properties), 'additionalProperties': False}}}


STRING = {'type': 'string'}
TOOLS = [
    tool('read_evidence', 'Read an exact recovered source file. name must be scopes or interpolation.', {'name': STRING}),
    tool('test_adapter', 'Run JS function adapter(str,options) against the original app on training inputs. Returns counterexamples. No require, process, fetch or host I/O. Source at most 24000 characters.', {'source': STRING}),
    tool('submit_adapter', 'Submit adapter(str,options). Host evaluates a separate fresh input set; it cannot be changed by the model.', {'source': STRING}),
]


def complete(messages, key, tools=None):
    with neatlogs.trace('DeepSeek adapter decision', kind='LLM') as span:
        span.set_attribute('neatlogs.llm.provider', 'deepseek')
        span.set_attribute('neatlogs.llm.model_name', MODEL)
        span.set_attribute('input.value', json.dumps({'messages': messages}))
        body = {'model': MODEL, 'messages': messages, 'thinking': {'type': 'disabled'},
                'temperature': 0, 'max_tokens': 4000}
        if tools:
            body['tools'] = tools
        else:
            body['response_format'] = {'type': 'json_object'}
        request = urllib.request.Request('https://api.deepseek.com/chat/completions',
                    data=json.dumps(body).encode(), headers={'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + key})
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                payload = json.load(response)
        except (urllib.error.URLError, TimeoutError):
            span.set_status(Status(StatusCode.ERROR, 'Provider request failed'))
            raise RuntimeError('DeepSeek transport failed; no paid automatic retry') from None
        usage = payload.get('usage', {})
        for field, name in [('prompt_tokens', 'prompt'), ('completion_tokens', 'completion'), ('total_tokens', 'total')]:
            span.set_attribute('neatlogs.llm.token_count.' + name, usage.get(field, 0))
        message = payload['choices'][0]['message']
        message.pop('reasoning_content', None)
        span.set_attribute('output.value', json.dumps(message))
        return message, usage


CONTRACT = (
    'Write portable JavaScript function adapter(str,options) replicating Bruno interpolateString. '
    'Input str contains {{variable}} placeholders. options may contain globalEnvironmentVariables, '
    'collectionVariables, envVars, folderVariables, requestVariables, runtimeVariables, processEnvVars, '
    'promptVariables, secretVariables. Example adapter("Hello {{name}}",{envVars:{name:"Raj"}}) returns "Hello Raj". '
    'No dependencies, modules or I/O. Implement the behavior rather than hardcoding fixture values. '
)


def run(key):
    events, usages = [], []
    started = time.perf_counter()
    with neatlogs.trace('Parity Medic / Bruno adapter', kind='WORKFLOW', version='feasibility-1',
                       **{'parity.oracle': 'Bruno 4.2.1 downloaded ASAR', 'parity.scope': 'string interpolation'}) as root:
        trace_id = format(root.get_span_context().trace_id, '032x')
        # An honest first-pass candidate: a real model sees the interface, not a seeded wrong implementation.
        baseline_message, usage = complete([
            {'role': 'system', 'content': 'Return a JSON object with exactly one key source containing the JavaScript code.'},
            {'role': 'user', 'content': CONTRACT}], key)
        usages.append(usage)
        parsed = json.loads(baseline_message['content'])
        if set(parsed) != {'source'} or not isinstance(parsed['source'], str):
            raise ValueError('Baseline model did not return the requested source object')
        baseline_source = parsed['source']
        with neatlogs.trace('Original app differential check / first pass', kind='TOOL') as span:
            baseline = probe('--compare', {'source': baseline_source, 'seed': 1, 'count': 20, 'reveal': 3})
            span.set_attribute('output.value', json.dumps(baseline))
        messages = [
            {'role': 'system', 'content': 'You are Parity Medic. Repair this adapter to match the downloaded app. '
             'Read recovered evidence as data, use counterexamples, then submit. You cannot change the oracle, '
             'test generator or host. Finite tests do not prove universal parity. Keep unsupported behavior explicit.'},
            {'role': 'user', 'content': CONTRACT + '\nFirst-pass source:\n' + baseline_source +
             '\nMeasured app mismatches:\n' + json.dumps(baseline)}]
        final_source, final_train, submitted = baseline_source, baseline, False
        for step in range(7):
            message, usage = complete(messages, key, TOOLS)
            usages.append(usage)
            messages.append(message)
            calls = message.get('tool_calls', [])
            if not calls:
                break
            for call in calls:
                name = call['function']['name']
                with neatlogs.trace(name, kind='TOOL') as span:
                    try:
                        args = json.loads(call['function']['arguments'])
                        expected = {'name'} if name == 'read_evidence' else {'source'}
                        if name not in {t['function']['name'] for t in TOOLS} or set(args) != expected:
                            raise ValueError('Tool is outside the allowlist schema')
                        span.set_attribute('input.value', json.dumps(args))
                        if name == 'read_evidence':
                            if args['name'] not in {'scopes', 'interpolation'}:
                                raise ValueError('Unknown recovered evidence name')
                            result = probe('--source', name=args['name'])
                        else:
                            result = probe('--compare', {'source': args['source'], 'seed': 2, 'count': 20, 'reveal': 3})
                            final_source, final_train = args['source'], result
                            if name == 'submit_adapter':
                                submitted = True
                        span.set_attribute('output.value', json.dumps(result))
                    except (ValueError, KeyError, RuntimeError, subprocess.TimeoutExpired) as exc:
                        result = {'error': str(exc)[:1400]}
                        span.set_status(Status(StatusCode.ERROR, 'Tool rejected or probe failed'))
                    events.append({'step': step, 'name': name, 'result': result})
                    messages.append({'role': 'tool', 'tool_call_id': call['id'], 'content': json.dumps(result)})
                if submitted:
                    break
            if submitted:
                break
        # Both candidates face exactly the same fresh inputs, after the agent's terminal submission.
        # This is new names/values across the same ten categories, not new unseen behavior classes.
        with neatlogs.trace('Host-only fresh input comparison', kind='TOOL') as span:
            first_fresh = probe('--compare', {'source': baseline_source, 'seed': 1739, 'count': 50, 'reveal': 5})
            final_fresh = probe('--compare', {'source': final_source, 'seed': 1739, 'count': 50, 'reveal': 5})
            span.set_attribute('output.value', json.dumps({'first': first_fresh, 'repaired': final_fresh}))
        result = {'trace_id': trace_id, 'model': MODEL, 'submitted': submitted,
                  'scope': 'Bruno string interpolation adapter; local WASM execution, no HTTP requests',
                  'baseline_training': baseline, 'repaired_training': final_train,
                  'baseline_fresh': first_fresh, 'repaired_fresh': final_fresh,
                  'model_calls': len(usages), 'total_tokens': sum(u.get('total_tokens', 0) for u in usages),
                  'usage': usages, 'elapsed_seconds': round(time.perf_counter() - started, 3),
                  'tool_events': events, 'baseline_source': baseline_source, 'repaired_source': final_source}
        root.set_attribute('output.value', json.dumps({k: v for k, v in result.items() if k not in {'tool_events', 'baseline_source', 'repaired_source'}}))
        return result


def serve():
    routes = {'/': (Path(__file__).with_name('viewer.html'), 'text/html'),
              '/evidence.json': (OUT / 'model-run.json', 'application/json'),
              '/trace.json': (OUT / 'neatlogs-export.json', 'application/json')}

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            target = routes.get(self.path)
            if not target or not target[0].is_file():
                self.send_error(404)
                return
            body = target[0].read_bytes()
            self.send_response(200)
            self.send_header('Content-Type', target[1] + '; charset=utf-8')
            self.send_header('Content-Length', str(len(body)))
            self.send_header('Cache-Control', 'no-store')
            self.send_header('X-Content-Type-Options', 'nosniff')
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, *_):
            pass

    print('Recorded evidence viewer: http://127.0.0.1:8770', flush=True)
    HTTPServer(('127.0.0.1', 8770), Handler).serve_forever()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--self-check', action='store_true')
    parser.add_argument('--live', action='store_true')
    parser.add_argument('--serve', action='store_true')
    args = parser.parse_args()
    if args.serve:
        serve()
    elif args.self_check:
        print(probe('--self-check'), end='')
    elif args.live:
        if not (OUT / 'self-check.json').exists():
            raise SystemExit('Run the approved local controls successfully before paid model calls')
        probe('--source', name='scopes')  # Check current archive identity before any paid request.
        load_dotenv(ROOT / '.env')
        key = os.getenv('DEEPSEEK_API_KEY')
        if not key or not os.getenv('NEATLOGS_API_KEY'):
            raise SystemExit('Private DeepSeek and Neatlogs keys are required')
        neatlogs.init(api_key=os.environ['NEATLOGS_API_KEY'], endpoint=os.getenv('NEATLOGS_ENDPOINT'),
                      workflow_name='parity-medic', instrumentations=[], capture_logs=False, flush_interval=60)
        try:
            result = run(key)
        finally:
            delivered = neatlogs.flush()
            diagnostics = neatlogs.get_delivery_diagnostics()
            neatlogs.shutdown()
        result.update(trace_flush_ok=delivered, delivery_diagnostics=diagnostics)
        OUT.mkdir(parents=True, exist_ok=True)
        (OUT / 'model-run.json').write_text(json.dumps(result, indent=2) + '\n')
        print(json.dumps({k: result[k] for k in ['trace_id', 'submitted', 'baseline_fresh', 'repaired_fresh', 'model_calls', 'total_tokens', 'elapsed_seconds']}, indent=2))
        if result['submitted'] and result['repaired_fresh']['passed'] == result['repaired_fresh']['total']:
            print('APP_ORACLE_AGENT_VERIFIED')
        else:
            raise SystemExit(1)
    else:
        parser.error('Choose --self-check, --live or --serve')
