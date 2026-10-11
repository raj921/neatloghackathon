"""Short SQLite transactions; no transaction spans model or guest execution."""
import json
import sqlite3
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


class Store:
    def __init__(self, path: Path):
        self.path = path
        path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
        with self.connection() as c:
            c.execute('PRAGMA journal_mode=WAL')
            c.executescript(Path(__file__).with_name('migrations').joinpath('001.sql').read_text())
        path.chmod(0o600)

    @contextmanager
    def connection(self):
        c = sqlite3.connect(self.path, timeout=10)
        c.row_factory = sqlite3.Row
        c.execute('PRAGMA foreign_keys=ON')
        try:
            with c:
                yield c
        finally:
            c.close()

    def recover(self) -> None:
        with self.connection() as c:
            rows=c.execute("SELECT id FROM runs WHERE state IN ('queued','verifying','repairing')").fetchall()
        for row in rows:
            self.update(row['id'], state='interrupted', error='Server restarted. Start a new attempt; no paid automatic retry.')
            self.event(row['id'], 'interrupted', 'Interrupted by server restart. Evidence preserved.')

    def create(self, title: str, contract: str, payload: dict, key: str, digest: str) -> tuple[dict, bool]:
        with self.connection() as c:
            c.execute('BEGIN IMMEDIATE')
            previous = c.execute('SELECT * FROM operations WHERE key=?', (key,)).fetchone()
            if previous:
                if previous['digest'] != digest:
                    raise ValueError('Idempotency key was already used with different input.')
                run_id, created = previous['run_id'], False
            else:
                run_id, created = uuid4().hex, True
                stamp = now()
                c.execute('INSERT INTO runs VALUES(?,?,?,?,?,?,?,0)',
                          (run_id, title, contract, 'queued', stamp, stamp, json.dumps(payload)))
                c.execute('INSERT INTO operations VALUES(?,?,?)', (key, run_id, digest))
        return self.get(run_id), created

    def get(self, run_id: str) -> dict | None:
        with self.connection() as c:
            row = c.execute('SELECT * FROM runs WHERE id=?', (run_id,)).fetchone()
            if not row:
                return None
            result = dict(row)
            result.update(json.loads(result.pop('payload')))
            result['events'] = [dict(e) | {'details': json.loads(e['details'])} for e in
                                c.execute('SELECT * FROM events WHERE run_id=? ORDER BY seq', (run_id,))]
            return result

    def list(self) -> list[dict]:
        with self.connection() as c:
            return [dict(r) for r in c.execute('SELECT id,title,contract,state,created_at,updated_at FROM runs ORDER BY created_at DESC LIMIT 100')]

    def update(self, run_id: str, *, state: str | None = None, **changes) -> dict:
        with self.connection() as c:
            c.execute('BEGIN IMMEDIATE')
            r = c.execute('SELECT payload,state FROM runs WHERE id=?', (run_id,)).fetchone()
            if not r:
                raise KeyError(run_id)
            # Cancellation wins over a late worker/model response.
            if r['state'] == 'cancelled':
                return self.get(run_id)
            payload = json.loads(r['payload'])
            payload.update(changes)
            c.execute('UPDATE runs SET payload=?,state=?,updated_at=?,revision=revision+1 WHERE id=?',
                      (json.dumps(payload), state or r['state'], now(), run_id))
        return self.get(run_id)

    def event(self, run_id: str, kind: str, message: str, details: dict | None = None) -> None:
        with self.connection() as c:
            c.execute('INSERT INTO events(run_id,created_at,kind,message,details) VALUES(?,?,?,?,?)',
                      (run_id, now(), kind, message, json.dumps(details or {})))
