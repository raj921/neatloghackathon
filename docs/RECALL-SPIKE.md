# Recall Relay: first feasibility verdict

October 11, 2026. Question: can a real tool-using model contain an official recall in a test retailer, including a bundle, excluded near-match, missing identifiers and a lost acknowledgement?

**Verdict: feasible on this narrow fixture; not yet a submission-ready or proven winning product.** The baseline already succeeds. Do not claim that the guards improved the agent's classification accuracy.

## What actually ran

- CPSC recall **10706 / 26-399**, retrieved from the [official API](https://www.saferproducts.gov/RestWebServices/Recall?ProductName=Power%20Banks&format=json). The [official notice](https://www.cpsc.gov/Recalls/2026/Shenzhen-Baihang-Recalls-VEEKTOMX-Mini-Power-Banks-Due-to-Fire-and-Burn-Hazards-Sold-on-Amazon) identifies VEEKTOMX VT103 power banks without a physical serial number on the lower-right back casing. Page image captions say VT03 while the description says VT103; that discrepancy is disclosed in model context. The spike does not resolve a VT03 item.
- Real `deepseek-flash` calls decide which tools to invoke and with which arguments. Fixed goal, seven allowlisted tools, 12-call ceiling and 2,200 output-token cap per call. No shell, file writes, arbitrary network requests or outbound messages are exposed to the model.
- **Synthetic** stock, receiving observations, quantities, orders and customer drafts. This is not a retailer integration, physical inspection or real recall response.
- An injected fault commits a stock decision but loses its acknowledgement. The model reads the operation outcome and continues; the fixture does not prescribe that sequence.
- Five independently scored stock decisions: two holds, two exclusions and one review awaiting a casing photo. Correct order dispositions and exactly two customer drafts are also checked. Nothing was sent.
- The verifier lives in host code outside the model's tool surface. This is a tool-permission boundary, not an operating-system sandbox or protection against a person editing the repository.

## Measured model runs

| Run | Correct lots | Orders / recipients | Duplicate mutations | Calls | Tokens | Seconds |
| --- | --- | --- | --- | --- | --- | --- |
| Baseline, seed 1 | 5/5 | Correct | 0 | 8 | 25,423 | 12.520 |
| Guarded, seed 1 | 5/5 | Correct | 0 | 8 | 25,007 | 14.310 |
| Guarded, seed 2 | 5/5 | Correct | 0 | 8 | 24,564 | 13.028 |
| Baseline, seed 3 | 5/5 | Correct | 0 | 8 | 25,647 | 13.738 |
| Guarded, seed 3 | 5/5 | Correct | 0 | 7 | 21,464 | 10.208 |

Seed 2/3 change quantities, aliases and a serial observation. They retain the same recall, fixture IDs and expected label categories. These are **not independent held-out recall types**. One shorter guarded run is an observation, not evidence of a repeatable efficiency gain.

Estimated DeepSeek inference cost was **$0.0013–$0.0018 per run**, using reported cache-hit/cache-miss/output tokens and the [October 11 published Sunday off-peak rates](https://api-docs.deepseek.com/quick_start/pricing/). This is not an invoice or total operating cost. Neatlogs shows a different cost estimate (e.g. $0.0078027 for guarded seed 3); use the provider-token calculation, with its stated rate date, for this prototype's economics. No provider billing account readback was performed.

The deterministic fault replay checks show a concrete backend improvement: replaying the same timed-out request creates **2 mutations in the baseline and 1 in guarded mode**. Both real-model baselines avoided that defect by checking the operation outcome. Do not present the deterministic replay as a failed model run.

Runnable checks also reject uninspected mutations, an invalid mixed batch, unknown tools and incomplete closure. Draft text is recorded for human inspection; recipient correctness is checked automatically, but the verifier does not prove every sentence medically or legally correct.

## Neatlogs evidence

Readback confirmed finalized model/tool traces for:

- Guarded seed 1: `91a02d47f7f03dedf0d3f8b30f626263`, 21 spans / 25,007 tokens.
- Guarded seed 2: `1988b4d404b3b869247297566daeab73`, 21 spans / 24,564 tokens.
- Baseline seed 3: `d2b313db9195b1e8f18119d6fb128bd2`, 21 spans / 25,647 tokens.
- Guarded seed 3: `78ed52f18fd05a80230441848255861e`, 20 spans / 21,464 tokens.

Safe public-API exports are under `docs/evidence/`. Baseline seed 1 is locally recorded but its remote trace readback was still unconfirmed at the final check. Some traces took several minutes to appear despite successful SDK flush; transport success alone is not readback proof. The last two runs reported zero SDK queue drops and export failures. Flush batching was lengthened, but a causal delivery fix is not established.

Neatlogs labels these traces `ERROR` because they include the deliberately failed tool acknowledgement. Host verification records successful containment separately. The injected fault remains visible in the trace rather than being hidden to make it green.

## Artifacts and execution

```sh
.venv/bin/python prototypes/recall-relay/agent.py --self-check
.venv/bin/python prototypes/recall-relay/agent.py --mode guarded --seed 3
```

Private keys are loaded from `.env`; they never enter the model messages, walkthrough, Git or evidence files. Re-running a seed replaces its evidence JSON; preserve earlier runs separately before further comparisons.

`prototypes/recall-relay/state-walkthrough.html` is a self-contained **simulation**, with free-play controls and three guided scenarios. Its scripts were executed with a minimal DOM harness: premature actions were blocked and retry applied one mutation. A visual browser audit is still outstanding. It does not display live model decisions; actual run JSON is the primary evidence.

The prototype is captured on `codex/recall-relay-prototype`. No framework or production frontend was selected. State survives tool calls within one process; it does **not** survive a process restart. A durable case/operation store is still needed to support that claim.

## What would make this competitive

The [current brief](https://neatlogs.com/hackathon) weights agent execution 30%, sponsor use 25%, demo 20%, building in public 15%, usefulness/originality 10%. Existing recall products already scan inventory and hold orders; differentiation must be demonstrated through evidence handling and safe recovery.

1. Test a second, materially different official recall and fresh fixture labels, including contradictory source text and an ambiguous identifier. Get a genuine failing baseline and a verified improvement if one exists; do not manufacture the result.
2. Add durable operation receipts and demonstrate interruption/resume without repeating a stock action. Keep unresolved evidence visible and fulfilment blocked.
3. Obtain feedback from a retailer or operations person; the business problem has not been validated by a target user.
4. Finish genuine Entire checkpoint or entire-graph evidence and a cfo.ai plan covering pricing, inference/infra costs, revenue and runway. Installed tools and user-confirmed account setup are not these artifacts.
5. Prepare a three-minute demo, public build posts and a public repository containing only safe product evidence. The current repo remains private; no public post or submission has been made.

Planned submission window: October 12, 7:00–11:55 PM IST; the event page says the final cutoff will be announced on Discord.
