# Operate Parity Medic

Parity Medic is a working single-operator local product. It compares a JavaScript adapter with two deterministic functions in Bruno 4.2.1, repairs mismatches with a bounded model loop, and exports evidence. It does not send the prepared HTTP request. Public hosting, multiple users and arbitrary app reconstruction are outside this release.

## Start

Prerequisites: Python 3.11, uv, npm and a supported Node 22 installation. The bootstrap installs the project-local Node specified by the existing setup lock. The pinned macOS application ZIP is treated as an inert archive; the verifier also works with those JavaScript bytes on other platforms, although this delivery was tested on macOS only.

```sh
sh scripts/bootstrap-product.sh
.venv/bin/python -m uvicorn app.main:create_app --factory --host 127.0.0.1 --port 8780 --workers 1 --no-access-log
```

Open http://127.0.0.1:8780. Opening recorded evidence makes no model request. New verification compares the sample or supplied source locally. A mismatch can be repaired after the provider disclosure. The HTTP API can also request `action: repair` so a violated contract triggers the loop automatically; an already matching or unsupported contract makes no model call.

Bootstrap installs a hash-locked Python environment and the committed npm dependency lock, downloads the official Bruno 4.2.1 release if absent, verifies both ZIP and ASAR digests, and extracts only the named archive member. It never launches Bruno, logs in to sponsors or provisions cloud resources. Downloads can take several minutes. A digest mismatch stops setup.

## Provider and secrets

Copy `.env.example` to `.env` if necessary. Local verification needs no AI key. Live repair uses `DEEPSEEK_API_KEY` or the overriding `PARITY_MODEL_API_KEY`. Change `PARITY_MODEL_ENDPOINT` and `PARITY_MODEL` to replace the provider with a chat-completions service supporting function tools. DeepSeek has a provider-specific non-thinking, required-tool option; other providers use their default tool behavior and the host requests a tool action if the model replies with prose. Restart after changes. A configured key is not a successful connection test.

Optional `NEATLOGS_API_KEY` and `NEATLOGS_ENDPOINT` enable metadata tracing. The browser receives readiness flags, not credentials. Custom source and inputs remain local for verification; live repair sends them and counterexamples to the model provider. Neatlogs receives event/usage metadata, not the source or custom input. Proof downloads contain the input and source: use synthetic data for shared records.

Limits: one worker, at most five active attempts, eight model calls per repair, six tools per model response, 5,000 output tokens per call, 100,000-character model context and no automatic provider retry. A context or transport failure preserves a failed attempt. Cancellation prevents further calls and acceptance of an in-flight result; it cannot reverse provider charges already incurred. Provider cost in trace readback is the tracing service's estimate, not an invoice.

## Storage, recovery and backup

Default storage is `.local/product/parity.sqlite3`, with WAL and short transactions. `PARITY_DATABASE` accepts an absolute private path. Store files are mode 600; use a directory accessible only to the operator. Database payloads are not encrypted. Restart changes all unfinished attempts to Interrupted; it does not restart paid work. Reopen history or explicitly start a new attempt. Every repair is a new run; the parent remains inspectable. Idempotency keys bind request content and parent so a repeated operation does not duplicate paid work.

Run exactly **one server process and one worker**. Do not use `--reload`, multiple Uvicorn workers or share the SQLite file with another running server. Queue ownership is process-local. Graceful shutdown waits for the active worker. For backup, stop the server and copy the database; alternatively use SQLite's online backup API. Keep backups private. The reversible migration files are under `app/migrations`; the down migration deletes product history and must be applied only after a backup.

## Authenticated remote operator mode

This release is locally tested. It has no public deployment receipt. Before binding a non-loopback interface, configure a random `PARITY_ACCESS_TOKEN` of at least 24 characters and the exact HTTPS `PARITY_PUBLIC_ORIGIN`, then place it behind a trusted TLS reverse proxy. Do not enable unrestricted forwarded headers. Keep the backend port private. Public origin without a suitable token/HTTPS fails startup. Cookie sessions are HttpOnly, SameSite Strict and Secure in remote mode. Login attempts are limited per connecting address; a reverse proxy should enforce its own limit as well.

Writes require a server-issued CSRF value, same-origin browser context and a bounded JSON body. Host allowlists, strict asset routes, CSP and sanitized validation errors cover the workbench boundary. This is one shared operator identity, not tenant isolation, per-user authorization, a production penetration test or a horizontally scalable service. Provider configuration is trusted server configuration. Rotate the operator token and provider keys on compromise; restart the server after rotation.

## API

Authenticated OpenAPI is at `/api/v1/openapi.json`. Main routes:

| Route | Purpose |
| --- | --- |
| GET `/api/v1/session` | CSRF value and operator authentication state |
| POST `/api/v1/login` | Operator-token login |
| GET `/api/v1/config` | Readiness and declared scope |
| GET `/api/v1/runs` | Most recent 100 attempts |
| POST `/api/v1/runs` | Verify or repair; requires unique `Idempotency-Key` |
| GET `/api/v1/runs/{id}` | Full durable comparison and events |
| POST `/api/v1/runs/{id}/repair` | New child repair; custom inputs need `send_data: true` |
| POST `/api/v1/runs/{id}/cancel` | Cancel active work |
| GET `/api/v1/runs/{id}/adapter` | Export verified current source, with Bruno's full MIT notice |
| GET `/api/v1/runs/{id}/proof` | Export source, measured outputs, mutations and scope |

Only a host comparison can produce Verified. Adapter export also checks the source digest. Imported completed evidence is explicitly Recorded; reverify before exporting through the API. Unsupported random/auth/binary/path-parameter workflows stop for review. Generated fresh values remain within the same declared behavior categories; finite agreement is not universal parity.

## Verification

The two acceptance commands were inspected and explicitly approved by the user. The local suite uses the real pinned oracle and synthetic HTTP inputs, with no paid calls. The live check uses up to eight calls and writes its actual evidence under `app/evidence`.

```sh
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/product_live_check.py
```

The second command incurs provider usage; do not run it as a default startup or ordinary CI check. Local tests are appropriate for CI once the verified archive and pinned dependencies are available. See `GATES.md` and `REVIEW.md` for acceptance evidence and remaining boundaries.
