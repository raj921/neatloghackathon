# Parity Medic

A developer-agent workbench that repairs compatibility adapters against an application's shipped behavior. Start a comparison, inspect the mismatch, let the agent read and test the original code, and download the independently checked result with evidence.

**Working local product:** http://127.0.0.1:8780 while the server is running. Request preparation improved **55/80 → 80/80** on fresh inputs across sixteen declared categories; another independently selected 80 inputs also matched. Three real DeepSeek calls used 28,418 tokens. These are finite generated comparisons against Bruno 4.2.1, not universal app compatibility or a general success rate.

```sh
sh scripts/bootstrap-product.sh
.venv/bin/python -m uvicorn app.main:create_app --factory --host 127.0.0.1 --port 8780 --workers 1 --no-access-log
```

Local verification makes no model call. Live repair needs a private model key and explicit provider-data consent in the interface. Recorded examples are labelled and do not execute again when opened. The workbench includes original-source inspection with fingerprints, before/current matrix navigation, concrete difference paths, exact-copy controls and Cmd/Ctrl+K search. The product includes durable history, input/source editing, comparison and mutation evidence, bounded repair, cancellation, review states, provider configuration and adapter/proof downloads.

- [Operating guide and API](docs/product/OPERATING.md)
- [Architecture and trust boundaries](docs/product/ARCHITECTURE.md)
- [Review and actual delivery evidence](docs/product/REVIEW.md)
- [Acceptance ledger](docs/product/GATES.md)
- [Latest UI and backend verification](docs/product/workbench-improvements/REVIEW.md)
- [Design system](DESIGN.md) and [saved reference decisions](design-references/parity-medic/README.md)

Neatlogs hosted readback confirms the product trace is finalized with three LLM calls and eight spans. Entire Graph supplied product source-review evidence. The repository became public on October 12. The actual cfo.ai plan and workbook are exported; a Neatlogs critical incident was investigated, reviewed and resolved against recorded rerun evidence. The final [2:58 demo](https://parity-medic-demo.vercel.app/demo.mp4) includes all three sponsors and is public on Vercel alongside the [business plan](https://parity-medic-demo.vercel.app/business-plan.pdf) and [financial workbook](https://parity-medic-demo.vercel.app/financial-model.xlsx). This deployment hosts media; the interactive backend remains local. The [official quote submission](https://x.com/RajKuma39078041/status/2109680625846534477) includes all three sponsor tags and the final native video. The mandatory form showed SUBMISSION RECEIVED at 21:54 IST on October 12; [receipt](docs/submission/SUBMISSION.md). No AWS resource has been provisioned. See the dated [build log](hackathon.md) and [submission checklist](docs/submission/CHECKLIST.md) for current evidence.

## Preserved research

The original [Parity Medic spike](prototypes/rea-parity/README.md) remains unchanged. Its real interpolation repair improved 25/50 to 50/50 across ten categories. The [research decision](docs/rea-research/DECISION.md) explains how the user's REA repository supplied static artifact evidence and how the downloaded Bruno implementation supplies the oracle.

The completed product is on `codex/parity-medic-product`. Earlier research is on `codex/rea-parity-spike`; the earlier Recall Relay experiment remains below.

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
