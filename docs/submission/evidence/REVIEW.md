# Sponsor evidence review · October 12, 2026

## cfo.ai

Ari generated the business plan, native scenarios and financial workbook in the existing account from `docs/product/BUSINESS-PLAN-INPUT.md` plus explicitly hypothetical assumptions. The actual downloaded PDF has 14 pages. Its prices, account counts, costs and cash are proposals, not observed traction or bank balances.

Downloaded PDF and XLSX SHA-256 values match `cfo-provenance.json`. PDF page 2 and the workbook's `Judging summary` agree on the six delivery/customer scenarios. The PDF includes pricing, complete cost bridges, revenue, repair-cost sensitivity and conditional runway. At zero accounts and after reserving $1,500 from hypothetical $5,000 cash, runway is 3.78 months local or 2.06 hosted. Positive steady-state cash flow is not a funded acquisition plan.

The report refers to an `Export notes` sheet, but the downloaded workbook has no sheet with that name. Treat the workbook as exported planning output; no independent certification of every formula is claimed. Ari's provenance describes its own checks. The independent download review here checked file hashes, PDF text completeness and the displayed scenario summary.

Public shared plan: https://cfo.ai/s/jmbAAAxR7or4ofo6

## Neatlogs critical incident

Incident: `15b2ca92-b68d-46b9-82bd-0e1bdcecf35b`.

https://app.neatlogs.com/incidents/15b2ca92-b68d-46b9-82bd-0e1bdcecf35b

The actual investigation found repeated 5,000-output-token calls and no successful adapter tool submission in the failed traces. Its report inferred invalid generated code and an infinite loop and suggested increasing the token cap. Those inferences do not match the recorded repository diagnosis. Two AI-chat correction attempts failed with connection errors; the native incident investigation completed, and a review correction was then successfully posted to its root-cause comments.

The actual diagnostic output records 5,000 reasoning tokens and no accepted adapter. The loop was bounded and cancelled. The local diagnostic snapshot records five completed calls; remote failure usage includes a sixth in-flight call. These are separate measurement boundaries.

The implemented correction disables DeepSeek thinking and requires tool calls while retaining the 5,000-token cap. Successful remote trace `7fa65df88286d4f7ff6bc9835c77fb10` contains three calls plus adapter test and submission spans. `app/evidence/request-live.json` records the host's 55/80 → 80/80 improvement and separate 80/80 replay.

The incident was marked resolved October 12 on that reviewed evidence. This is a retrospective investigation of October 11 runs; it did not cause the earlier implementation change. It is not proof of a new deployed production run. `neatlogs-incident-readback.txt` preserves the provider's report; this review corrects its unsupported causal claims.

## Entire

`app/evidence/entire-product-search.json` is the real source graph/search output used during implementation. Formatting was expanded for readability without changing values. Its first result points to model configuration and tracing in `app/service.py`. Graph evidence is distinct from a captured checkpoint; no checkpoint is claimed.
