#!/bin/sh
# Install setup tools only. Credentials and account sign-in remain separate.
set -eu
TASK_ROOT="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
cd "$TASK_ROOT"
command -v uv >/dev/null
command -v npm >/dev/null
uv venv --allow-existing --python 3.11 .venv
uv pip install --python .venv/bin/python -r requirements.txt
mkdir -p .local/tools .local/bin
cp tooling/package.json .local/tools/package.json
cp tooling/package-lock.json .local/tools/package-lock.json
npm ci --prefix .local/tools
curl -fsSL https://static-assets.crustdata.com/cli/install.sh -o .local/crustdata-install.sh
CRUSTDATA_VERSION=0.2.19 CRUSTDATA_NO_MODIFY_PATH=1 \
  CRUSTDATA_INSTALL_DIR="$TASK_ROOT/.local/bin" sh .local/crustdata-install.sh
if ! command -v entire >/dev/null; then
  brew install --cask entireio/tap/entire
fi
if [ ! -f .env ]; then
  cp .env.example .env
  chmod 600 .env
fi
printf '%s\n' 'Tools installed. See docs/SETUP.md for account status and verification.'
