"""Acceptance checks exercise the real original app and HTTP trust boundaries; no paid calls."""
import json
import os
import tempfile
import time
import unittest
from pathlib import Path
from unittest.mock import patch

from fastapi.testclient import TestClient

os.environ.setdefault('NEATLOGS_API_KEY', '')
from app.main import NewRun, create_app, validate_case
from app.service import engine, Service, MODEL_ENDPOINT
from app.store import Store


class OriginalBehaviorTests(unittest.TestCase):
    def test_original_positive_and_negative_controls(self):
        result=engine('controls')
        self.assertEqual(result['request_positive'],32)
        self.assertEqual(result['bindings'],['undefined','undefined','undefined'])
        bad=engine('verify',{'contract':'request','source':'function adapter(r){return r}','count':16,'seed':918})
        self.assertEqual(bad['decision'],'mismatch')
        self.assertLess(bad['passed'],bad['total'])

    def test_exported_spike_adapter_on_new_inputs(self):
        source=json.loads(Path('docs/rea-research/evidence/model-run.json').read_text())['repaired_source']
        result=engine('verify',{'contract':'string','source':source,'count':40,'seed':81829})
        self.assertEqual(result['passed'],40)
        self.assertEqual(result['decision'],'verified')

    def test_input_mutation_is_part_of_contract(self):
        source=json.loads(Path('docs/rea-research/evidence/model-run.json').read_text())['repaired_source']
        source=source.replace('function adapter(', 'function originalAdapter(')+'\nfunction adapter(s,o){const result=originalAdapter(s,o);o.changed=true;return result;}'
        result=engine('verify',{'contract':'string','source':source,'count':10,'seed':111})
        self.assertEqual(result['passed'],0)

    def test_random_and_unsupported_requests_stop(self):
        random=engine('verify',{'contract':'string','source':'function adapter(s){return s}','custom':{'str':'{{$randomUUID}}','options':{}},'count':10})
        self.assertEqual(random['decision'],'needs_review')
        auth=engine('verify',{'contract':'request','source':'function adapter(r){return r}','custom':{'request':{'url':'http://fixture.local','headers':{},'basicAuth':{}},'options':{}},'count':16})
        self.assertEqual(auth['decision'],'needs_review')

    def test_infinite_guest_is_interrupted(self):
        started=time.monotonic()
        result=engine('verify',{'contract':'string','source':'function adapter(){while(true){}}','count':10})
        self.assertEqual(result['decision'],'mismatch')
        self.assertIn('interrupted',result['cases'][0]['actual']['error'])
        self.assertLess(time.monotonic()-started,15)


class RepairProtocolTests(unittest.TestCase):
    def test_provider_requires_an_action_with_thinking_disabled(self):
        if 'api.deepseek.com' not in MODEL_ENDPOINT: self.skipTest('Provider-specific control')
        response=unittest.mock.MagicMock()
        response.__enter__.return_value.read.return_value=json.dumps({'choices':[{'message':{'role':'assistant','content':'','tool_calls':[]},'finish_reason':'stop'}],'usage':{'total_tokens':1}}).encode()
        with tempfile.TemporaryDirectory() as tmp:
            service=Service(Store(Path(tmp)/'runs.sqlite3'))
            try:
                with patch.dict(os.environ,{'PARITY_MODEL_API_KEY':'synthetic-test-key'}),patch('urllib.request.urlopen',return_value=response) as transport:
                    service.call_model([{'role':'user','content':'control'}],[{'type':'function','function':{'name':'submit_adapter'}}])
                    body=json.loads(transport.call_args.args[0].data)
                    self.assertEqual(body['thinking'],{'type':'disabled'})
                    self.assertEqual(body['tool_choice'],'required')
            finally: service.pool.shutdown()

    def test_wrong_submission_is_withheld_by_independent_host(self):
        with tempfile.TemporaryDirectory() as tmp:
            store=Store(Path(tmp)/'runs.sqlite3');service=Service(store)
            record,_=store.create('Bad submission','string',{'source':'function adapter(s){return s}','seed':19},'negative-submit','bad')
            message={'role':'assistant','content':'','tool_calls':[{'id':'control','type':'function','function':{'name':'submit_adapter','arguments':json.dumps({'source':'function adapter(s){return s}'})}}]}
            try:
                with patch.object(service,'call_model',return_value=(message,{'total_tokens':1})):
                    service.repair(record['id'],record,engine('verify',{'contract':'string','source':record['source'],'count':10}),time.monotonic())
                result=store.get(record['id']);self.assertEqual(result['state'],'needs_review');self.assertLess(result['result']['passed'],80)
            finally: service.pool.shutdown()


class ApiTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.env=patch.dict(os.environ,{'NEATLOGS_API_KEY':'','PARITY_ACCESS_TOKEN':'','PARITY_PUBLIC_ORIGIN':''})
        self.env.start()
        self.app=create_app(Path(self.tmp.name)/'runs.sqlite3')
        self.client=TestClient(self.app)
        self.client.__enter__()
        self.csrf=self.client.get('/api/v1/session').json()['csrf']

    def tearDown(self):
        self.client.__exit__(None,None,None)
        self.env.stop();self.tmp.cleanup()

    def post(self,path,body,key='test-operation'):
        return self.client.post('/api/v1'+path,json=body,headers={'X-Parity-Csrf':self.csrf,'Idempotency-Key':key})

    def test_real_local_journey_and_durable_history(self):
        source=json.loads(Path('docs/rea-research/evidence/model-run.json').read_text())['repaired_source']
        body={'contract':'string','source':source,'title':'Actual local journey'}
        first=self.post('/runs',body)
        self.assertEqual(first.status_code,202)
        run_id=first.json()['id']
        repeat=self.post('/runs',body)
        self.assertEqual(repeat.json()['id'],run_id)
        conflicting=self.post('/runs',body|{'title':'changed'})
        self.assertEqual(conflicting.status_code,409)
        deadline=time.monotonic()+20
        while time.monotonic()<deadline:
            result=self.client.get('/api/v1/runs/'+run_id).json()
            if result['state'] not in {'queued','verifying'}: break
            time.sleep(.1)
        self.assertEqual(result['state'],'verified')
        self.assertEqual(result['model_calls'],0)
        adapter=self.client.get('/api/v1/runs/'+run_id+'/adapter')
        self.assertEqual(adapter.status_code,200)
        self.assertIn('export { adapter }',adapter.text)
        self.assertEqual(Store(Path(self.tmp.name)/'runs.sqlite3').get(run_id)['state'],'verified')
        self.assertEqual(self.client.get('/api/v1/runs/'+run_id+'/proof').json()['result']['decision'],'verified')

    def test_origin_csrf_validation_and_path_controls(self):
        self.assertEqual(self.client.post('/api/v1/runs',json={}).status_code,403)
        hostile=self.client.post('/api/v1/runs',json={},headers={'Origin':'https://attacker.example','X-Parity-Csrf':self.csrf})
        self.assertEqual(hostile.status_code,403)
        self.assertEqual(self.post('/runs',{'custom':{'request':{'url':42}}}).status_code,422)
        self.assertEqual(self.post('/runs',{'unknown':'field'}).status_code,422)
        self.assertEqual(self.post('/login',[]).status_code,422)
        large=self.client.post('/api/v1/runs',content='x'*65537,headers={'X-Parity-Csrf':self.csrf,'Content-Type':'application/json'})
        self.assertEqual(large.status_code,413)
        self.assertEqual(self.client.get('/.env').status_code,404)
        self.assertEqual(self.client.get('/assets/../../.env').status_code,404)
        self.assertEqual(self.client.get('/api/v1/config',headers={'Host':'attacker.example'}).status_code,400)
        self.assertIn("script-src 'self'",self.client.get('/').headers['content-security-policy'])
        # A spoofed loopback Host does not grant an unauthenticated remote client access.
        with TestClient(self.app,client=('203.0.113.19',12345)) as remote:
            self.assertEqual(remote.get('/api/v1/runs').status_code,401)

    def test_pending_adapter_export_is_denied_and_cancellation_wins(self):
        record,_=self.app.state.store.create('Cancel control','string',{'source':'function adapter(s){return s}'},'cancel','x')
        run_id=record['id']
        self.assertEqual(self.client.get('/api/v1/runs/'+run_id+'/adapter').status_code,409)
        self.assertEqual(self.post('/runs/'+run_id+'/cancel',{}).status_code,200)
        self.app.state.store.update(run_id,state='verified',source='late result')
        self.assertEqual(self.app.state.store.get(run_id)['state'],'cancelled')

    def test_restart_marks_unfinished_attempts_interrupted(self):
        store=self.app.state.store
        record,_=store.create('Restart control','string',{'source':'function adapter(s){return s}'},'restart','y')
        store.recover()
        self.assertEqual(store.get(record['id'])['state'],'interrupted')

    def test_authenticated_operator_session(self):
        with patch.dict(os.environ,{'PARITY_ACCESS_TOKEN':'operator-test-token-24-characters'}):
            app=create_app(Path(self.tmp.name)/'auth.sqlite3')
            with TestClient(app) as client:
                sess=client.get('/api/v1/session').json()
                self.assertFalse(sess['authenticated'])
                self.assertEqual(client.get('/api/v1/runs').status_code,401)
                headers={'X-Parity-Csrf':sess['csrf']}
                self.assertEqual(client.post('/api/v1/login',json={'token':'wrong'},headers=headers).status_code,401)
                response=client.post('/api/v1/login',json={'token':'operator-test-token-24-characters'},headers=headers)
                self.assertEqual(response.status_code,200)
                self.assertIn('HttpOnly',response.headers['set-cookie'])
                self.assertEqual(client.get('/api/v1/runs').status_code,200)


if __name__=='__main__': unittest.main()
