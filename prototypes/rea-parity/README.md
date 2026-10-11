# Parity Medic feasibility spike

Real DeepSeek repairs an adapter against Bruno's downloaded interpolation implementation. Recorded result: **25/50 → 50/50** fresh input matches across ten declared categories. See [decision and evidence](../../docs/rea-research/DECISION.md).

The app archive and dependencies are local research inputs, not committed project code. Generated candidate code has no filesystem, network or process bindings in QuickJS. The original oracle and the candidate use separate interpreter contexts. There is no production adapter, external HTTP call or deployment.

## Existing workspace

```sh
.venv/bin/python prototypes/rea-parity/agent.py --self-check
.venv/bin/python prototypes/rea-parity/agent.py --live
.venv/bin/python prototypes/rea-parity/agent.py --serve
```

The viewer is at http://127.0.0.1:8770 and serves only three allowlisted read-only routes. It shows the saved run; opening it makes no model call. `--live` uses private DeepSeek/Neatlogs credentials from the ignored `.env`, with up to eight model requests and no automatic transport retry. Local checks must pass first. The two acceptance commands were explicitly approved by the user through the Unlazy review flow.

## Reconstruct research dependencies

Requires the repository's Python setup, Node 22.19+ and npm. In this workspace Node lives at `.local/tools/node_modules/node/bin/node`.

```sh
PATH="$PWD/.local/tools/node_modules/node/bin:$PATH" npm install --prefix .local/research/rea-runtime --ignore-scripts --omit=dev --no-audit --no-fund rea-agents@6.4.0 quickjs-emscripten@0.32.0
curl -L --fail -o .local/research/bruno-4.2.1.zip https://github.com/usebruno/bruno/releases/download/v4.2.1/bruno_4.2.1_arm64_mac.zip
```

Verify and extract the app archive without launching or installing the app:

```python
from pathlib import Path
import hashlib, zipfile, shutil
p = Path('.local/research/bruno-4.2.1.zip')
assert hashlib.sha256(p.read_bytes()).hexdigest() == '0573c46a7049c4def8a55a78edf6fe6202cae2ea6c8475da8cfc819408455ae9'
dest = Path('.local/research/bruno-4.2.1/app.asar')
dest.parent.mkdir(parents=True, exist_ok=True)
with zipfile.ZipFile(p) as z, z.open('Bruno.app/Contents/Resources/app.asar') as f, dest.open('wb') as out:
    shutil.copyfileobj(f, out)
```

The checker additionally pins the ASAR digest. REA statically examines a seven-file slice; it does not prove runtime IPC behavior. All recorded limitations are retained in the summary. Full local application Evidence lives under `.local/research/parity/`; compact summaries are committed.

## Attribution and limits

Bruno is an external MIT-licensed reference application. `repaired-adapter.js` was generated during the hackathon using its recovered source; [BRUNO-LICENSE.txt](BRUNO-LICENSE.txt) preserves the upstream notice. REA and QuickJS are existing dependencies, not code we claim to have invented.

The proof covers deterministic JSON inputs to string interpolation. It excludes Faker/random/time values, special JavaScript objects, full request execution and future app versions. Its fresh inputs change names and values within the same categories. The random UUID control demonstrates an oracle that must be replaced with semantic checks rather than forced exact-output equality.
