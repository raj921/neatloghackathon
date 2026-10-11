// Throwaway spike: a downloaded app is the oracle; candidate code gets no host bindings.
import { createHash } from 'node:crypto';
import { readFile, writeFile, mkdir } from 'node:fs/promises';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { execFile } from 'node:child_process';
import { promisify } from 'node:util';
import assert from 'node:assert/strict';
import { extractFile } from '../../.local/research/rea-runtime/node_modules/@electron/asar/lib/asar.js';
import { getQuickJS } from '../../.local/research/rea-runtime/node_modules/quickjs-emscripten/dist/index.mjs';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '../..');
const ARCHIVE = resolve(ROOT, '.local/research/bruno-4.2.1/app.asar');
const WORK = resolve(ROOT, '.local/research/parity');
const EVIDENCE = resolve(ROOT, 'docs/rea-research/evidence');
const APP_SHA = 'fe9b4c89660ac3f1291707746f76b9b5850edda368a5e0250055687ab02ec767';
const sha = bytes => createHash('sha256').update(bytes).digest('hex');
const PATHS = {
  scopes: 'src/ipc/network/interpolate-string.js',
  interpolation: 'node_modules/@usebruno/common/src/interpolate/index.ts',
  common: 'node_modules/@usebruno/common/dist/cjs/index.js',
  lodash: 'node_modules/lodash/lodash.js',
};
const slicePaths = ['package.json', 'src/index.js', 'src/preload.js',
  PATHS.scopes, 'src/ipc/network/interpolate-vars.js',
  'src/ipc/network/prepare-request.js', 'src/ipc/network/index.js'];
let sources;
async function load() {
  if (sources) return sources;
  assert.equal(sha(await readFile(ARCHIVE)), APP_SHA, 'Downloaded app identity changed');
  sources = Object.fromEntries(Object.entries(PATHS).map(([name, path]) =>
    [name, extractFile(ARCHIVE, path).toString()]));
  return sources;
}

async function prepare() {
  await load();
  await mkdir(EVIDENCE, { recursive: true });
  const slice = resolve(WORK, 'bruno-slice');
  const manifest = { version: '4.2.1', asar_sha256: APP_SHA, scope: 'selected request-related modules; not the entire app', files: [] };
  for (const path of slicePaths) {
    const bytes = extractFile(ARCHIVE, path);
    const dest = resolve(slice, path);
    await mkdir(dirname(dest), { recursive: true });
    await writeFile(dest, bytes);
    manifest.files.push({ path, bytes: bytes.length, sha256: sha(bytes) });
  }
  for (const [name, path] of Object.entries(PATHS)) {
    manifest.files.push({ path, role: name, sha256: sha(sources[name]), bytes: Buffer.byteLength(sources[name]) });
  }
  await writeFile(resolve(EVIDENCE, 'bruno-manifest.json'), JSON.stringify(manifest, null, 2) + '\n');
  // No app launch, MCP registration, credential inheritance, or recovered-code execution.
  const { stdout } = await promisify(execFile)(process.execPath, [
    resolve(ROOT, '.local/research/rea-runtime/node_modules/rea-agents/scripts/rea.mjs'),
    'analyze-javascript-application', slice, '--json',
  ], { cwd: ROOT, env: { PATH: process.env.PATH }, timeout: 180000, maxBuffer: 50 * 1024 * 1024 });
  const result = JSON.parse(stdout);
  assert.ok(result.normalized_result?.graph, 'REA did not return application Evidence');
  await writeFile(resolve(WORK, 'rea-application.json'), stdout);
  const n = result.normalized_result;
  const summary = { evidence_id: result.evidence_id, ...manifest,
    root_artifact_sha256: n.root_artifact_sha256, graph_id: n.graph.graph_id,
    statistics: n.statistics, summary: n.summary, limitations: n.limitations };
  await writeFile(resolve(EVIDENCE, 'rea-summary.json'), JSON.stringify(summary, null, 2) + '\n');
  return summary;
}

const QuickJS = await getQuickJS();
function context() {
  const runtime = QuickJS.newRuntime();
  runtime.setMemoryLimit(64 * 1024 * 1024);
  runtime.setMaxStackSize(1024 * 1024);
  let deadline = Date.now() + 3000;
  runtime.setInterruptHandler(() => Date.now() > deadline);
  const vm = runtime.newContext();
  const evaluate = code => {
    deadline = Date.now() + 3000;
    const result = vm.evalCode(code);
    if (result.error) {
      const error = vm.dump(result.error); result.error.dispose();
      throw new Error(String(error?.message || error));
    }
    const value = vm.dump(result.value); result.value.dispose(); return value;
  };
  return { evaluate, close() { vm.dispose(); runtime.dispose(); } };
}

function moduleCode(name, source) {
  return `modules[${JSON.stringify(name)}] = (() => { const module={exports:{}}; const exports=module.exports;
    const require = id => { if (!(id in modules)) throw new Error('No module: '+id); return modules[id]; };
    ${source}\n;return module.exports; })();`;
}
const ORACLE_GLOBALS = 'globalThis.crypto={subtle:{}}; const modules=Object.create(null);';
async function oracle() {
  const s = await load(); const c = context();
  try {
    // Bundled common initializes a crypto capability reference. No crypto is used by this deterministic scope.
    // Deliberately no implementation: random/Faker/crypto behavior is outside the oracle's supported contract.
    c.evaluate(ORACLE_GLOBALS);
    c.evaluate(moduleCode('lodash', s.lodash));
    c.evaluate(moduleCode('@usebruno/common', s.common));
    c.evaluate(moduleCode('scopes', s.scopes));
    c.evaluate('const adapter=modules.scopes.interpolateString;');
    return c;
  } catch (error) { c.close(); throw error; }
}

function cases(seed, count) {
  // Host-side generated JSON inputs, not a hand-written expected-output table.
  const rows = [];
  for (let i = 0; i < count; i++) {
    const k = `key_${seed}_${i}`, v = `value_${seed}_${i}`, r = { str: '{{' + k + '}}', options: {} };
    switch (i % 10) {
      case 0: r.options = { collectionVariables: { [k]: 'collection' }, envVars: { [k]: 'environment' }, requestVariables: { [k]: v } }; break;
      case 1: r.options = { runtimeVariables: { [k]: 'runtime' }, promptVariables: { [k]: 'prompt' }, secretVariables: { [k]: v } }; break;
      case 2: r.str = 'prefix/' + r.str; break; // unresolved placeholders must survive
      case 3: r.str = '{{user.name}}/{{user.age}}'; r.options = { envVars: { user: { name: v, age: 0 } } }; break;
      case 4: r.str = '{{user.name}}'; r.options = { envVars: { 'user.name': v, user: { name: 'nested' } } }; break;
      case 5: r.options = { envVars: { [k]: '{{next}}', next: v } }; break;
      case 6: r.str = '{{a}}/{{b}}/{{c}}'; r.options = { envVars: { a: 0, b: false, c: null } }; break;
      case 7: r.options = { envVars: { [k]: { nested: v } } }; break;
      case 8: r.options = { envVars: { [k]: '{{process.env.DEST}}' }, processEnvVars: { DEST: v } }; break;
      case 9: r.str = ''; r.options = { envVars: { [k]: v } }; break;
    }
    rows.push({ category: i % 10, ...r });
  }
  return rows;
}

function invoke(c, row) {
  return c.evaluate(`(() => {const input=${JSON.stringify(row)}; const before=JSON.stringify(input);
    const output=adapter(input.str,input.options); return {output,mutated:JSON.stringify(input)!==before};})()`);
}
async function compare(source, seed, count, reveal = 3) {
  assert.equal(typeof source, 'string'); assert.ok(source.length <= 24000, 'Candidate is too large');
  const original = await oracle(), candidate = context();
  let passed = 0; const failures = [];
  try {
    candidate.evaluate(source);
    for (const row of cases(seed, count)) {
      const expected = invoke(original, row); let actual;
      try { actual = invoke(candidate, row); } catch (e) { actual = { error: e.message }; }
      const equal = JSON.stringify(expected) === JSON.stringify(actual);
      if (equal) passed++;
      else if (failures.length < reveal) failures.push({ category: row.category, input: row, original: expected, candidate: actual });
    }
    return { passed, total: count, failures, oracle: 'Bruno 4.2.1 shipped interpolateString in isolated QuickJS', asar_sha256: APP_SHA };
  } finally { original.close(); candidate.close(); }
}

async function stabilityProbe() {
  const c = await oracle();
  try {
    const row = { str: '{{$randomUUID}}', options: {} };
    const observations = [invoke(c, row), invoke(c, row)];
    assert.notDeepEqual(observations[0], observations[1], 'Random oracle control unexpectedly matched');
    return { input: row, observations, decision: 'needs_semantic_oracle',
      reason: 'The original itself is nondeterministic. Exact-output equality is not a valid acceptance oracle.' };
  } finally { c.close(); }
}

async function selfCheck() {
  const s = await load();
  const equivalent = ORACLE_GLOBALS + '\n' + moduleCode('lodash', s.lodash) +
    moduleCode('@usebruno/common', s.common) + moduleCode('scopes', s.scopes) +
    'function adapter(str, options) { return modules.scopes.interpolateString(str, options); }';
  // Positive control uses the same original code, not a claim about a repaired adapter.
  const original = await oracle(); const twin = context();
  try {
    twin.evaluate(equivalent);
    for (const row of cases(999, 20)) assert.deepEqual(invoke(twin, row), invoke(original, row));
  } finally { original.close(); twin.close(); }
  const bad = await compare('function adapter(str,options){ return str; }', 999, 20);
  assert.ok(bad.passed < bad.total && bad.failures.length > 0, 'Known wrong candidate escaped');
  const c = context();
  try {
    assert.equal(c.evaluate('[typeof process,typeof require,typeof fetch].join(",")'), 'undefined,undefined,undefined');
    assert.throws(() => c.evaluate('while(true){}'), /interrupted/);
  } finally { c.close(); }
  const summary = await prepare();
  assert.ok(summary.statistics.parsed_javascript_files > 0);
  const result = { positive_control: '20/20 identical original-code outputs', negative_control: bad,
    candidate_host_bindings: [], infinite_loop: 'interrupted within runtime deadline',
    rea_evidence_id: summary.evidence_id, rea_static_only: true,
    unsupported_probe: await stabilityProbe() };
  try {
    const recorded = JSON.parse(await readFile(resolve(EVIDENCE, 'model-run.json'), 'utf8'));
    const exported = await readFile(resolve(ROOT, 'prototypes/rea-parity/repaired-adapter.js'), 'utf8');
    assert.ok(exported.endsWith(recorded.repaired_source + '\n'), 'Exported candidate differs from the measured model output');
    const replay = await compare(exported, 2227, 50, 3);
    assert.equal(replay.passed, replay.total, 'Exported adapter regression');
    result.exported_adapter_replay = { source_sha256: sha(exported), ...replay };
  } catch (error) {
    if (error.code !== 'ENOENT') throw error;
    // First run has no exported adapter yet; oracle controls still run independently.
  }
  await writeFile(resolve(EVIDENCE, 'self-check.json'), JSON.stringify(result, null, 2) + '\n');
  console.log('PARITY_CONTROLS_VERIFIED');
}

const mode = process.argv[2];
if (mode === '--self-check') await selfCheck();
else if (mode === '--source') {
  const s = await load(); const name = process.argv[3];
  assert.ok(['scopes', 'interpolation'].includes(name));
  console.log(JSON.stringify({ path: PATHS[name], sha256: sha(s[name]), source: s[name] }));
} else if (mode === '--compare') {
  let data = ''; for await (const chunk of process.stdin) data += chunk;
  const input = JSON.parse(data);
  console.log(JSON.stringify(await compare(input.source, input.seed, input.count, input.reveal)));
} else { throw new Error('Use --self-check, --source or --compare'); }
