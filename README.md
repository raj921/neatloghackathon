# neatHack / developer agent feasibility workspace

The current recommendation is **Parity Medic**: repair a model-generated adapter by comparing it with a downloaded application's actual code. A real run improved from 25/50 to 50/50 matching fresh inputs across ten declared categories. See [the research decision](docs/rea-research/DECISION.md), [the runnable spike](prototypes/rea-parity/README.md), and the recorded evidence viewer at `http://127.0.0.1:8770` while its local server is running. This is a narrow feasibility proof, not a finished production app.

```sh
.venv/bin/python prototypes/rea-parity/agent.py --serve
```

The new experiment is on `codex/rea-parity-spike`. The earlier Recall Relay experiment remains below and on its original branch.

Sponsor setup plus a throwaway **Recall Relay** feasibility spike, started October 11 after the user's go-ahead. Real CPSC data, DeepSeek tool decisions and Neatlogs tracing; a clearly labelled synthetic store. No application framework or production retailer integration.

See [the spike verdict](docs/RECALL-SPIKE.md). The prototype is kept on `codex/recall-relay-prototype`.

```sh
.venv/bin/python prototypes/recall-relay/agent.py --self-check
.venv/bin/python prototypes/recall-relay/agent.py --mode guarded --seed 3
```

Open `prototypes/recall-relay/state-walkthrough.html` directly for a self-contained **simulation** of the state transitions. It does not call the model or replay actual runs. Actual run records are under `docs/evidence/`.

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
