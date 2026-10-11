// Promoted from the measured spike. Original and candidate have separate bounded QuickJS runtimes.
import { createHash } from 'node:crypto';
import { readFile } from 'node:fs/promises';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import assert from 'node:assert/strict';
import { extractFile } from '../.local/research/rea-runtime/node_modules/@electron/asar/lib/asar.js';
import { getQuickJS } from '../.local/research/rea-runtime/node_modules/quickjs-emscripten/dist/index.mjs';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const ARCHIVE = resolve(ROOT, '.local/research/bruno-4.2.1/app.asar');


const APP_SHA = 'fe9b4c89660ac3f1291707746f76b9b5850edda368a5e0250055687ab02ec767';
const sha = bytes => createHash('sha256').update(bytes).digest('hex');
const PATHS = {
  scopes: 'src/ipc/network/interpolate-string.js',
  interpolation: 'node_modules/@usebruno/common/src/interpolate/index.ts',
  request: 'src/ipc/network/interpolate-vars.js',
  common: 'node_modules/@usebruno/common/dist/cjs/index.js',
  lodash: 'node_modules/lodash/lodash.js',
};
let sources;
async function load() {
  if (sources) return sources;
  assert.equal(sha(await readFile(ARCHIVE)), APP_SHA, 'Downloaded app identity changed');
  sources = Object.fromEntries(Object.entries(PATHS).map(([name, path]) =>
    [name, extractFile(ARCHIVE, path).toString()]));
  return sources;
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


const CATEGORY_NAMES = ['Scope precedence','Runtime and secret precedence','Unresolved variables','Nested values','Literal dotted keys','Recursive variables','Falsy values','Object values','Environment references','Empty text'];
const REQUEST_NAMES = ['URL and headers','JSON object body','JSON string escaping','GraphQL body','Form values','Multipart values','Header name substitution','Runtime precedence','Iteration precedence','Missing variables','Nested variables','Empty body','JSON content type casing','Process references','Proxy fields','Auth field removal'];
function generated(contract, seed, count) {
  const rows=[];
  for(let i=0;i<count;i++) {
    const k=`key_${seed}_${i}`,v=`value_${seed}_${i}`;
    if(contract==='string') {
      const row={id:`case-${i}`,category:CATEGORY_NAMES[i%10],str:`{{${k}}}`,options:{}};
      switch(i%10) {
        case 0:row.options={collectionVariables:{[k]:'collection'},envVars:{[k]:'environment'},requestVariables:{[k]:v}};break;
        case 1:row.options={runtimeVariables:{[k]:'runtime'},promptVariables:{[k]:'prompt'},secretVariables:{[k]:v}};break;
        case 2:row.str='prefix/'+row.str;break;
        case 3:row.str='{{user.name}}/{{user.age}}';row.options={envVars:{user:{name:v,age:0}}};break;
        case 4:row.str='{{user.name}}';row.options={envVars:{'user.name':v,user:{name:'nested'}}};break;
        case 5:row.options={envVars:{[k]:'{{next}}',next:v}};break;
        case 6:row.str='{{a}}/{{b}}/{{c}}';row.options={envVars:{a:0,b:false,c:null}};break;
        case 7:row.options={envVars:{[k]:{nested:v}}};break;
        case 8:row.options={envVars:{[k]:'{{process.env.DEST}}'},processEnvVars:{DEST:v}};break;
        case 9:row.str='';break;
      }
      rows.push(row);continue;
    }
    const row={id:`case-${i}`,category:REQUEST_NAMES[i%16],request:{url:`http://fixture.local/orders/{{${k}}}`,headers:{'Content-Type':'application/json','X-Customer':`{{${k}}}`},data:{name:`{{${k}}}`}},options:{envVars:{[k]:v}}};
    const r=row.request,o=row.options;
    switch(i%16) {
      case 1:r.data={items:[`{{${k}}}`],amount:0,enabled:false};break;
      case 2:r.data='{"name":"{{'+k+'}}"}';o.envVars[k]=v+'"\\\n';break;
      case 3:r.mode='graphql';r.data={query:'query { user(name:"{{'+k+'}}") { id } }',variables:'{"name":"{{'+k+'}}"}'};o.envVars[k]=v+'"';break;
      case 4:r.headers={'Content-Type':'application/x-www-form-urlencoded'};r.data=[{name:'name',value:`{{${k}}}`}];break;
      case 5:r.headers={'Content-Type':'multipart/form-data'};r.data=[{name:'files',value:[`{{${k}}}`,'fixed']}];break;
      case 6:r.headers={'{{header}}':`{{${k}}}`};o.envVars.header='X-Resolved';break;
      case 7:r.collectionVariables={[k]:'collection'};r.requestVariables={[k]:'request'};o.runtimeVariables={[k]:v};break;
      case 8:r.runnerIterationDetails={iterationData:{[k]:v}};o.runtimeVariables={[k]:'runtime'};break;
      case 9:o.envVars={};break;
      case 10:r.data={name:'{{user.name}}'};o.envVars={'user.name':v,user:{name:'nested'}};break;
      case 11:r.data='';break;
      case 12:r.headers={'cOnTeNt-TyPe':'application/json'};break;
      case 13:o.envVars={[k]:'{{process.env.DEST}}'};o.processEnvVars={DEST:v};break;
      case 14:r.proxy={protocol:'http',hostname:`{{${k}}}`,port:'8080'};break;
      case 15:r.auth={username:'sample',password:'synthetic-only'};break;
    }
    rows.push(row);
  }
  return rows;
}
function unsupported(contract,row) {
  const str=JSON.stringify(row);
  if(/\{\{\s*\$/.test(str))return 'Random, clock and Faker placeholders need a semantic oracle. Exact equality would mislead.';
  if(contract==='request'){
    const r=row.request;
    const fields=['basicAuth','oauth2','awsv4config','digestConfig','wsse','ntlmConfig','edgeGridConfig','oauth1config'];
    if(fields.some(k=>k in r)||r.pathParams?.length||['grpc','ws'].includes(r.mode))return 'This contract supports JSON URL/header/body preparation. Auth, path parameters, gRPC and WebSocket need another verified harness.';
    if(r.proxy?.auth)return 'Proxy authentication is outside the supported synthetic request contract.';
  }
  return null;
}
async function originalRequest() {
  const s=await load(),c=context();
  try {
    c.evaluate(ORACLE_GLOBALS+'const Buffer={isBuffer:()=>false};');
    c.evaluate(moduleCode('lodash',s.lodash));c.evaluate(moduleCode('@usebruno/common',s.common));
    c.evaluate(moduleCode('request',s.request));c.evaluate('const adapter=(request,options={})=>modules.request(request,options.envVars||{},options.runtimeVariables||{},options.processEnvVars||{},options.promptVariables||{},options.secretVariables||{});');
    return c;
  }catch(e){c.close();throw e;}
}
function execute(c,contract,row) {
  const json=JSON.stringify(JSON.stringify(row));
  return c.evaluate(`(()=>{const row=JSON.parse(${json});const before=JSON.stringify(row);const output=adapter(row.${contract==='request'?'request':'str'},row.options||{});return {output,mutated:JSON.stringify(row)!==before,input_after:row};})()`);
}
function canonical(value) {
  if(Array.isArray(value))return value.map(canonical);
  if(value&&typeof value==='object')return Object.fromEntries(Object.keys(value).sort().map(k=>[k,canonical(value[k])]));
  return value;
}
async function verify(input) {
  assert.ok(['string','request'].includes(input.contract),'Unknown contract');
  assert.ok(typeof input.source==='string'&&input.source.length<=24000,'Adapter must be text, at most 24,000 characters');
  const count=input.count??32;assert.ok(Number.isInteger(count)&&count>0&&count<=100,'Case count must be 1–100');
  const rows=generated(input.contract,input.seed??1,count);
  if(input.custom)rows.unshift({...input.custom,id:'custom',category:'Your input'});
  const reasons=[...new Set(rows.map(r=>unsupported(input.contract,r)).filter(Boolean))];
  if(reasons.length)return {decision:'needs_review',reasons,passed:0,total:rows.length,cases:[]};
  const original=input.contract==='request'?await originalRequest():await oracle();
  const candidate=context();let passed=0;const results=[];let candidateError;
  try {
    try{candidate.evaluate(input.source)}catch(e){candidateError=e.message;}
    for(const row of rows){
      let expected,actual;
      try{expected=execute(original,input.contract,row)}catch(e){return {decision:'needs_review',reasons:['Original behavior could not be executed: '+e.message],passed:0,total:rows.length,cases:results};}
      if(candidateError)actual={error:candidateError};
      else try{actual=execute(candidate,input.contract,row)}catch(e){actual={error:e.message};candidateError=e.message;}
      const match=JSON.stringify(canonical(expected))===JSON.stringify(canonical(actual));if(match)passed++;
      results.push({id:row.id,category:row.category,input:row,reference:expected,actual,match});
    }
    return {decision:passed===rows.length?'verified':'mismatch',passed,total:rows.length,cases:results,source_sha256:sha(input.source),artifact_sha256:APP_SHA,seed:input.seed??1,
      scope:input.contract==='request'?'Bruno 4.2.1 deterministic JSON request preparation; no network transport':'Bruno 4.2.1 deterministic JSON string interpolation',
      limits:['Finite generated cases; not a formal proof.','Fresh names and values within documented behavior categories.','No random/time/Faker, binary, auth or path parameter parity.']};
  }finally{original.close();candidate.close();}
}
async function graphEvidence(input={}) {
  const record=JSON.parse(await readFile(resolve(ROOT,'app/evidence/rea-selection.json'),'utf8'));
  const path=input.contract==='string'?PATHS.scopes:PATHS.request;
  // Select from actual REA module identities, never invent a static edge or runtime execution.
  const nodes=record.selected_nodes.filter(n=>n.identity?.namespace==='source-module' && n.observations?.some(o=>o.properties?.path===path));
  assert.equal(nodes.length,1,'Supported request module is not uniquely identified in REA Evidence');
  const s=await load();
  assert.equal(nodes[0].identity.artifact_sha256,sha(input.contract==='string'?s.scopes:s.request),'REA source differs from current shipped module');
  return {evidence_id:record.evidence_id,graph_id:record.graph_id,parent_record_sha256:record.parent_record_sha256,authority:'static inference',selected_nodes:nodes.map(n=>({node_id:n.node_id??n.id,kind:n.kind,label:n.observations[0]?.label,identity:n.identity})),
    selection:'Supported contract selects module identity from the existing seven-file REA graph; not universal feature discovery.',limitations:record.limitations};
}
const mode=process.argv[2];let data='';for await(const chunk of process.stdin)data+=chunk;
try {
  const input=data?JSON.parse(data):{};
  if(mode==='verify')console.log(JSON.stringify(await verify(input)));
  else if(mode==='source'){const s=await load();assert.ok(['scopes','interpolation','request'].includes(input.name));console.log(JSON.stringify({path:PATHS[input.name],sha256:sha(s[input.name]),source:s[input.name]}));}
  else if(mode==='graph')console.log(JSON.stringify(await graphEvidence(input)));
  else if(mode==='controls'){const a=await originalRequest(),b=await originalRequest();let passed=0;try{for(const row of generated('request',882,32)){assert.deepEqual(execute(a,'request',row),execute(b,'request',row));passed++;}}finally{a.close();b.close();}const c=context();try{console.log(JSON.stringify({request_positive:passed,bindings:c.evaluate('[typeof process,typeof require,typeof fetch]')}));}finally{c.close();}}
  else if(mode==='identity'){await load();console.log(JSON.stringify({version:'4.2.1',sha256:APP_SHA,available:true}));}
  else if(mode==='bindings'){const c=context();try{console.log(JSON.stringify(c.evaluate('[typeof process,typeof require,typeof fetch]')));}finally{c.close();}}
  else throw new Error('Unknown engine operation');
}catch(e){console.error(String(e.message).slice(0,1200));process.exitCode=1;}
