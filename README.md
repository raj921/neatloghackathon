# neatHack setup workspace

Setup and credentials only. No product idea, UI, agent workflow, or application framework has been implemented.

See [the setup record](docs/SETUP.md) for verified accounts, tools, credential locations, remaining activation steps, and official references.

## Installed tools

- Python 3.11 environment: `.venv`
- Neatlogs SDK 1.4.26, boto3 1.43.111, python-dotenv 1.2.4
- Project-local Node 22.23.3, neatlogs-cli 0.2.0, and Neatlogs Codex hooks 0.1.1
- Entire CLI 0.11.4 with project Codex hooks
- Crustdata CLI 0.2.19

## Run setup tools

These commands load `.env` without displaying credential values:

```sh
.venv/bin/python scripts/tool.py neatlogs projects current
.venv/bin/python scripts/tool.py neatlogs traces list --limit 5
.venv/bin/python scripts/tool.py doctor --local --json
.venv/bin/python scripts/tool.py crustdata account credits --format json
sh scripts/neatlogs-codex doctor --project
entire status
.venv/bin/python scripts/tool.py aws sts get-caller-identity
```

`doctor --probe --json` sends a synthetic diagnostic trace to the configured Neatlogs project. It proves setup transport and readback, not application behavior.

To reinstall local tools, run `sh scripts/bootstrap.sh`. Reinstalling tools does not sign in to accounts or recreate credentials.

## Credentials

`.env`, `.secrets/`, `.local/`, and `.venv/` are ignored by Git. Neatlogs and Entire CLI login tokens use macOS Keychain. Do not add secrets, login links, transcripts, or credential screenshots to the repository.

AWS event access is configured in the separate `neathack` profile, restricted to `us-east-1`. The AWS tool command explicitly selects this profile and region. The organiser provides one shared $25 allowance for the team. See the setup record for permitted services and resource limits.
