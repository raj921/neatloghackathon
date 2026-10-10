"""Run setup tools with local credentials, without printing secret values."""
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

root = Path(__file__).resolve().parent.parent
load_dotenv(root / ".env")
os.chdir(root)
packages = root / ".local/tools/node_modules"
commands = {
    "aws": ["aws", "--profile", "neathack", "--region", "us-east-1"],
    "neatlogs": [str(packages / "node/bin/node"), str(packages / "neatlogs-cli/dist/bin.js")],
    "codex": [str(packages / "node/bin/node"), str(packages / "@neatlogs/codex/dist/cli.js")],
    "crustdata": [str(root / ".local/bin/crustdata")],
    "doctor": [str(root / ".venv/bin/python"), "-m", "neatlogs", "doctor"],
}
if len(sys.argv) < 2 or sys.argv[1] not in commands:
    raise SystemExit("Usage: tool.py aws|neatlogs|codex|crustdata|doctor [arguments]")
if sys.argv[1] == "neatlogs":
    # The readback CLI treats this name as a legacy service-account token.
    # The SDK project key is for ingestion; readback uses the saved OAuth profile.
    os.environ.pop("NEATLOGS_API_KEY", None)
command = commands[sys.argv[1]] + sys.argv[2:]
os.execvpe(command[0], command, os.environ)
