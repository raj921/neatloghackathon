-- UP: durable attempts and append-only events. Payload contains bounded synthetic/user data.
CREATE TABLE IF NOT EXISTS runs (
  id TEXT PRIMARY KEY, title TEXT NOT NULL, contract TEXT NOT NULL,
  state TEXT NOT NULL, created_at TEXT NOT NULL, updated_at TEXT NOT NULL,
  payload TEXT NOT NULL, revision INTEGER NOT NULL DEFAULT 0
);
CREATE INDEX IF NOT EXISTS runs_created ON runs(created_at DESC);
CREATE TABLE IF NOT EXISTS events (
  seq INTEGER PRIMARY KEY AUTOINCREMENT, run_id TEXT NOT NULL REFERENCES runs(id),
  created_at TEXT NOT NULL, kind TEXT NOT NULL, message TEXT NOT NULL, details TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS events_run_seq ON events(run_id, seq);
CREATE TABLE IF NOT EXISTS operations (
  key TEXT PRIMARY KEY, run_id TEXT NOT NULL REFERENCES runs(id), digest TEXT NOT NULL
);
PRAGMA user_version = 1;
