"""One-process local workbench; remote access requires an operator token and HTTPS proxy."""
import hashlib
import hmac
import json
import os
import secrets
import time
import threading
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Literal
from urllib.parse import urlparse

import neatlogs
from dotenv import load_dotenv
from fastapi import FastAPI, Header, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import FileResponse, JSONResponse, Response
from pydantic import BaseModel, ConfigDict, Field, JsonValue
from starlette.middleware.trustedhost import TrustedHostMiddleware

ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / '.env', override=False)
from app.service import MODEL, MODEL_ENDPOINT, Service, engine
from app.store import Store

WEB = ROOT / 'app/web'
DEFAULT_REQUEST_SOURCE = '''function adapter(request,options={}) {
  const vars={...(request.collectionVariables||{}),...(options.envVars||{}),...(request.requestVariables||{}),...(options.runtimeVariables||{})};
  const text=s=>typeof s==='string'?s.replace(/\\{\\{([^}]+)\\}\\}/g,(m,k)=>k in vars?String(vars[k]):m):s;
  const walk=x=>typeof x==='string'?text(x):Array.isArray(x)?x.map(walk):x&&typeof x==='object'?Object.fromEntries(Object.entries(x).map(([k,v])=>[k,walk(v)])):x;
  request.url=text(request.url);request.headers=walk(request.headers);request.data=walk(request.data);return request;
}'''


class NewRun(BaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str = Field(default='Bruno adapter', min_length=1, max_length=80)
    contract: Literal['string', 'request'] = 'request'
    source: str | None = Field(default=None, max_length=24000)
    custom: dict[str, JsonValue] | None = None
    action: Literal['verify', 'repair'] = 'verify'
    send_data: bool = False


class Login(BaseModel):
    model_config = ConfigDict(extra='forbid')
    token: str = Field(max_length=256)


class RepairOptions(BaseModel):
    model_config = ConfigDict(extra='forbid')
    send_data: bool = False


def validate_case(contract: str, custom: dict | None) -> None:
    if custom is None:
        return
    if len(json.dumps(custom)) > 12000:
        raise HTTPException(422, 'Custom input exceeds 12 KB.')
    def depth(x, level=0):
        if level > 12:
            raise HTTPException(422, 'Custom input exceeds 12 nesting levels.')
        if isinstance(x, dict):
            if any(k in {'__proto__','constructor','prototype'} for k in x):
                raise HTTPException(422, 'Prototype-related keys are outside this JSON contract.')
            for v in x.values(): depth(v, level+1)
        elif isinstance(x, list):
            for v in x: depth(v, level+1)
    depth(custom)
    allowed = {'request','options'} if contract=='request' else {'str','options'}
    if set(custom)-allowed or ('request' if contract=='request' else 'str') not in custom:
        raise HTTPException(422, 'Use exactly request/options or str/options for this contract.')
    if not isinstance(custom.get('options',{}), dict):
        raise HTTPException(422, 'Options must be a JSON object.')
    if contract=='request':
        r=custom['request']
        if not isinstance(r,dict) or not isinstance(r.get('url'),str) or not isinstance(r.get('headers',{}),dict):
            raise HTTPException(422, 'Request needs a URL string and a headers object.')
        if any(not isinstance(v,(str,int,float,bool,type(None))) for v in r.get('headers',{}).values()):
            raise HTTPException(422, 'Header values must be JSON scalars.')
    elif not isinstance(custom['str'],str):
        raise HTTPException(422, 'str must be a string.')


def default_source(contract: str) -> str:
    if contract=='request': return DEFAULT_REQUEST_SOURCE
    return json.loads((ROOT/'docs/rea-research/evidence/model-run.json').read_text())['baseline_source']


def create_app(db_path: Path | None = None) -> FastAPI:
    token = os.getenv('PARITY_ACCESS_TOKEN', '')
    public_origin = os.getenv('PARITY_PUBLIC_ORIGIN', '').rstrip('/')
    csrf = secrets.token_urlsafe(32)
    login_attempts, login_lock = {}, threading.Lock()
    store = Store(db_path or Path(os.getenv('PARITY_DATABASE', str(ROOT/'.local/product/parity.sqlite3'))))
    service = Service(store)

    @asynccontextmanager
    async def lifespan(app):
        if public_origin and (not public_origin.startswith('https://') or len(token)<24):
            raise RuntimeError('Remote mode requires HTTPS public origin and an operator token of at least 24 characters.')
        store.recover()
        if os.getenv('NEATLOGS_API_KEY'):
            neatlogs.init(api_key=os.environ['NEATLOGS_API_KEY'],endpoint=os.getenv('NEATLOGS_ENDPOINT'),
                          workflow_name='parity-medic-product',instrumentations=[],capture_logs=False,flush_interval=60)
        if not store.list():
            original=json.loads((ROOT/'docs/rea-research/evidence/model-run.json').read_text())
            run,_=store.create('Original interpolation research','string',{
                'kind':'recorded','source':original['repaired_source'],'initial_source':original['baseline_source'],
                'seed':1739,'baseline':original['baseline_fresh'],'result':original['repaired_fresh'],
                'model_calls':original['model_calls'],'total_tokens':original['total_tokens'],
                'elapsed_seconds':original['elapsed_seconds'],'trace_id':original['trace_id'],
                'trace_delivery':'remote_verified','artifact':{'version':'4.2.1','sha256':'fe9b4c89660ac3f1291707746f76b9b5850edda368a5e0250055687ab02ec767'},
                'limits':['Recorded spike: ten interpolation categories; different values within those categories.','This record was not executed by opening the product.']},'seed-recorded','research-v1')
            store.update(run['id'],state='verified')
            store.event(run['id'],'recorded','Imported actual completed DeepSeek research evidence. Opening this record makes no model call.')
        # Import completed acceptance evidence as an explicitly recorded attempt; never replay paid work.
        evidence_path=ROOT/'app/evidence/request-live.json'
        if evidence_path.exists():
            evidence=json.loads(evidence_path.read_text())
            payload={k:v for k,v in evidence.items() if k not in {'id','title','contract','state','created_at','updated_at','revision','events'}}
            payload.update(kind='recorded',recorded_request=True,recorded_run_id=evidence['id'])
            recorded,created=store.create('Request repair · recorded live run','request',payload,'seed-request-recorded',evidence['source_sha256'])
            if created:
                store.update(recorded['id'],state='verified')
                for event in evidence['events']:
                    store.event(recorded['id'],event['kind'],event['message'],event.get('details'))
                store.event(recorded['id'],'recorded','Imported actual completed product acceptance evidence. Event timestamps above reflect import; original timestamps and run ID are in the proof.',{'original_run_id':evidence['id'],'original_completed_at':evidence['updated_at']})
        yield
        service.pool.shutdown(wait=True, cancel_futures=False)
        if os.getenv('NEATLOGS_API_KEY'): neatlogs.shutdown()

    app = FastAPI(title='Parity Medic',version='1.0.0',lifespan=lifespan,docs_url=None,redoc_url=None,openapi_url=None)
    app.state.store,app.state.service=store,service
    hosts=['localhost','127.0.0.1']
    if db_path is not None: hosts.append('testserver')
    if public_origin: hosts.append(urlparse(public_origin).hostname)
    app.add_middleware(TrustedHostMiddleware,allowed_hosts=hosts)

    def authenticated(request: Request) -> bool:
        if not token:
            client=request.client.host if request.client else ''
            return not public_origin and (client in {'127.0.0.1','::1'} or (db_path is not None and client=='testclient'))
        value=request.headers.get('authorization','').removeprefix('Bearer ') or request.cookies.get('parity_session','')
        return hmac.compare_digest(value,token)

    @app.middleware('http')
    async def boundary(request: Request, call_next):
        expected=public_origin or str(request.base_url).rstrip('/')
        if request.method not in {'GET','HEAD','OPTIONS'}:
            if request.headers.get('origin') not in {None,expected} or request.headers.get('sec-fetch-site')=='cross-site':
                return JSONResponse({'error':{'code':'ORIGIN_REJECTED','message':'Open this action from your Parity Medic workbench.'}},403)
            if request.headers.get('x-parity-csrf')!=csrf:
                return JSONResponse({'error':{'code':'CSRF_REJECTED','message':'Reload the workbench before this action.'}},403)
            try: length=int(request.headers.get('content-length','0'))
            except ValueError: length=65537
            if length<0 or length>65536 or request.headers.get('transfer-encoding'):
                return JSONResponse({'error':{'code':'BODY_TOO_LARGE','message':'Request body exceeds 64 KB.'}},413)
            body = bytearray()
            async for chunk in request.stream():
                body.extend(chunk)
                if len(body)>65536:
                    return JSONResponse({'error':{'code':'BODY_TOO_LARGE','message':'Request body exceeds 64 KB.'}},413)
            request._body = bytes(body)
            if request.headers.get('content-type','').split(';')[0]!='application/json':
                return JSONResponse({'error':{'code':'JSON_REQUIRED','message':'Send a JSON request.'}},415)
        if request.url.path.startswith('/api/') and request.url.path not in {'/api/v1/session','/api/v1/login'} and not authenticated(request):
            return JSONResponse({'error':{'code':'UNAUTHORIZED','message':'Enter the operator token to open this workbench.'}},401)
        response=await call_next(request)
        response.headers.update({'X-Content-Type-Options':'nosniff','X-Frame-Options':'DENY','Referrer-Policy':'no-referrer',
            'Content-Security-Policy':"default-src 'self'; script-src 'self'; style-src 'self'; font-src 'self'; img-src 'self' data:; connect-src 'self'; frame-ancestors 'none'; base-uri 'none'; form-action 'self'",'Cache-Control':'no-store'})
        return response

    @app.exception_handler(HTTPException)
    async def http_error(_,exc):
        return JSONResponse({'error':{'code':str(exc.status_code),'message':str(exc.detail)}},exc.status_code)

    @app.exception_handler(RequestValidationError)
    async def validation_error(_,exc):
        # Do not echo rejected raw input, which can contain credentials.
        return JSONResponse({'error':{'code':'VALIDATION','message':'Check the contract, source length and input fields.'}},422)

    @app.get('/api/v1/session')
    def session(request: Request):
        return {'authenticated':authenticated(request),'login_required':bool(token),'csrf':csrf}

    @app.post('/api/v1/login')
    async def login(request: Request, body: Login):
        address=request.client.host if request.client else 'unknown'
        stamp=time.monotonic()
        with login_lock:
            for host in list(login_attempts):
                login_attempts[host]=[t for t in login_attempts[host] if stamp-t<60]
                if not login_attempts[host]: del login_attempts[host]
            attempts=login_attempts.setdefault(address,[])
            if len(attempts)>=10: raise HTTPException(429,'Wait a minute before another login attempt.')
            attempts.append(stamp)
        if not token or not hmac.compare_digest(body.token,token):
            raise HTTPException(401,'Operator token is incorrect.')
        response=JSONResponse({'ok':True})
        response.set_cookie('parity_session',token,httponly=True,samesite='strict',secure=bool(public_origin),max_age=28800)
        return response

    @app.get('/api/v1/config')
    def config():
        return {'model':MODEL,'provider':'DeepSeek' if 'deepseek.com' in MODEL_ENDPOINT else 'Compatible provider',
            'model_ready':bool(os.getenv('PARITY_MODEL_API_KEY') or os.getenv('DEEPSEEK_API_KEY')),
            'neatlogs_ready':bool(os.getenv('NEATLOGS_API_KEY')),'original_available':(ROOT/'.local/research/bruno-4.2.1/app.asar').is_file(),
            'max_model_calls':8,'max_output_tokens_per_call':5000,'mode':'authenticated operator' if token else 'local operator',
            'contracts':[{'id':'request','label':'Request preparation','description':'URL, headers, JSON, form and GraphQL bodies.'},
                         {'id':'string','label':'String interpolation','description':'Variables, scopes, dotted keys and JSON values.'}],
            'sponsors':{'neatlogs':'Configured' if os.getenv('NEATLOGS_API_KEY') else 'Not configured','entire':'Graph research evidence available','cfo':'Product plan not yet verified in cfo.ai'}}

    @app.get('/api/v1/runs')
    def runs(): return {'runs':store.list()}

    def get_run(run_id):
        run=store.get(run_id)
        if not run: raise HTTPException(404,'Attempt not found.')
        return run

    @app.get('/api/v1/runs/{run_id}')
    def run(run_id: str): return get_run(run_id)

    def start(body: NewRun,key: str,parent: str | None = None):
        if not key or len(key)>100: raise HTTPException(422,'A unique Idempotency-Key is required.')
        validate_case(body.contract,body.custom)
        if body.action=='repair':
            if body.custom and not body.send_data: raise HTTPException(422,'Confirm sending your input to the model provider before repair.')
            if not (os.getenv('PARITY_MODEL_API_KEY') or os.getenv('DEEPSEEK_API_KEY')): raise HTTPException(503,'Configure a model key on the server first.')
        source=body.source if body.source is not None else default_source(body.contract)
        if not source.strip(): raise HTTPException(422,'Adapter source cannot be empty.')
        digest=hashlib.sha256(json.dumps(body.model_dump() | {'parent_id':parent},sort_keys=True).encode()).hexdigest()
        payload={'kind':'live' if body.action=='repair' else 'local','source':source,'initial_source':source,'custom':body.custom,
                 'seed':secrets.randbelow(1_000_000),'parent_id':parent,'model_calls':0,'total_tokens':0,'trace_delivery':'not_sent'}
        try: result,created=store.create(body.title,body.contract,payload,key,digest)
        except ValueError as e: raise HTTPException(409,str(e)) from None
        if created:
            store.event(result['id'],'queued','Live repair queued.' if body.action=='repair' else 'Local verification queued. No model call.')
            try: service.enqueue(result['id'],body.action=='repair')
            except ValueError as e:
                store.update(result['id'],state='failed',error=str(e))
                raise HTTPException(429,str(e)) from None
        return result

    @app.post('/api/v1/runs',status_code=202)
    def new_run(body: NewRun,idempotency_key: str = Header(default='')):
        return start(body,idempotency_key)

    @app.post('/api/v1/runs/{run_id}/repair',status_code=202)
    async def repair(run_id: str,options: RepairOptions,idempotency_key: str = Header(default='')):
        previous=get_run(run_id)
        if previous['state'] in {'queued','verifying','repairing'}: raise HTTPException(409,'This attempt is still active.')
        body=NewRun(title=previous['title'],contract=previous['contract'],source=previous['source'],custom=previous.get('custom'),action='repair',send_data=options.send_data)
        return start(body,idempotency_key,parent=run_id)

    @app.post('/api/v1/runs/{run_id}/cancel')
    def cancel(run_id: str):
        previous=get_run(run_id)
        if previous['state'] not in {'queued','verifying','repairing'}: raise HTTPException(409,'Only an active attempt can be cancelled.')
        store.update(run_id,state='cancelled')
        store.event(run_id,'cancelled','Cancellation requested. An in-flight provider call may finish; its repair will not be accepted.')
        return get_run(run_id)

    @app.get('/api/v1/runs/{run_id}/proof')
    def proof(run_id: str):
        data=get_run(run_id)
        data.update(export_scope='Finite supported Bruno 4.2.1 contract; not universal parity',source_sha256=hashlib.sha256(data['source'].encode()).hexdigest())
        return JSONResponse(data,headers={'Content-Disposition':f'attachment; filename="parity-{run_id[:8]}-proof.json"'})

    @app.get('/api/v1/runs/{run_id}/adapter')
    def adapter(run_id: str):
        data=get_run(run_id)
        if data['state']!='verified': raise HTTPException(409,'This adapter has not passed the declared comparison.')
        if data.get('kind')=='recorded': raise HTTPException(409,'Reverify recorded research before exporting from this product.')
        if data['result'].get('source_sha256')!=hashlib.sha256(data['source'].encode()).hexdigest(): raise HTTPException(409,'Source digest no longer matches verification.')
        license_text=(ROOT/'prototypes/rea-parity/BRUNO-LICENSE.txt').read_text()
        code='// Bruno-compatible experimental adapter. Finite scope: see accompanying proof.\n'+''.join('// '+line+'\n' for line in license_text.splitlines())+data['source']+'\nexport { adapter };\n'
        return Response(code,media_type='text/javascript',headers={'Content-Disposition':f'attachment; filename="parity-{run_id[:8]}-adapter.mjs"'})

    @app.get('/api/v1/openapi.json')
    def schema(): return app.openapi()

    @app.get('/')
    def home(): return FileResponse(WEB/'index.html')

    @app.get('/assets/{filename:path}')
    def asset(filename: str):
        path=(WEB/filename).resolve()
        if not path.is_relative_to(WEB) or not path.is_file() or filename not in {'app.js','style.css','fonts/uncut-sans.woff2','fonts/LICENSE.txt'}:
            raise HTTPException(404,'Asset not found.')
        return FileResponse(path)

    return app
