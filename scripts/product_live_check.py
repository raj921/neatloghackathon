"""Inspected acceptance command: one actual durable request repair, maximum eight model calls.

Uses existing DeepSeek key and Neatlogs project. No posting, accounts, cloud deployment
or external request transport. Evidence written only under app/evidence.
"""
import json
import sys
import tempfile
import time
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from fastapi.testclient import TestClient
from app.main import create_app
from app.service import engine


def main():
    with tempfile.TemporaryDirectory() as tmp:
        app=create_app(Path(tmp)/'live.sqlite3')
        with TestClient(app) as client:
            session=client.get('/api/v1/session').json()
            if not session['authenticated']: raise RuntimeError('Run this local acceptance command without remote operator mode.')
            response=client.post('/api/v1/runs',json={'title':'Real request workflow repair','contract':'request','action':'repair'},
                                 headers={'X-Parity-Csrf':session['csrf'],'Idempotency-Key':'actual-request-repair-v1'})
            response.raise_for_status();run_id=response.json()['id']
            deadline=time.monotonic()+600
            while time.monotonic()<deadline:
                run=client.get('/api/v1/runs/'+run_id).json()
                if run['state'] not in {'queued','verifying','repairing'}: break
                time.sleep(.3)
            out=ROOT/'app/evidence';out.mkdir(exist_ok=True)
            if run['state']!='verified':
                (out/'request-failed.json').write_text(json.dumps(run,indent=2)+'\n')
            assert run['state']=='verified', {k:run.get(k) for k in ['state','error','model_calls','total_tokens']}
            assert 0<run['model_calls']<=8
            assert run['baseline']['passed']<run['baseline']['total']
            assert run['result']['passed']==run['result']['total']==80
            settle=time.monotonic()+10
            while run_id in app.state.service.jobs and time.monotonic()<settle: time.sleep(.1)
            run=client.get('/api/v1/runs/'+run_id).json()
            assert client.get('/api/v1/runs/'+run_id+'/adapter').status_code==200
            # Independently selected new seed replay of the actual exported candidate.
            replay=engine('verify',{'contract':'request','source':run['source'],'count':80,'seed':72619})
            assert replay['passed']==80
            out=ROOT/'app/evidence';out.mkdir(exist_ok=True)
            (out/'request-live.json').write_text(json.dumps(run|{'independent_replay':replay},indent=2)+'\n')
            (out/'request-adapter.mjs').write_text(client.get('/api/v1/runs/'+run_id+'/adapter').text)
            print(json.dumps({k:run.get(k) for k in ['id','trace_id','state','model_calls','total_tokens','elapsed_seconds']}))
            print('PRODUCT_LIVE_VERIFIED')


if __name__=='__main__': main()
