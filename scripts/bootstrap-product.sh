#!/bin/sh
# Install pinned local dependencies and verify an inert reference artifact. No model calls.
set -eu
TASK_ROOT="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
cd "$TASK_ROOT"
command -v uv >/dev/null
command -v npm >/dev/null
uv venv --allow-existing --python 3.11 .venv
uv pip install --python .venv/bin/python --require-hashes -r tooling/product-requirements.lock
mkdir -p .local/tools .local/research/rea-runtime
cp tooling/package.json tooling/package-lock.json .local/tools/
npm ci --prefix .local/tools --no-audit --no-fund
cp tooling/product-runtime/package.json tooling/product-runtime/package-lock.json .local/research/rea-runtime/
PATH="$TASK_ROOT/.local/tools/node_modules/node/bin:$PATH" npm ci --prefix .local/research/rea-runtime --ignore-scripts --omit=dev --no-audit --no-fund
.venv/bin/python scripts/prepare_reference.py
if [ ! -f .env ]; then cp .env.example .env; chmod 600 .env; fi
printf '%s\n' 'Local product dependencies ready. Add model credentials only for live repair; see docs/product/OPERATING.md.'
