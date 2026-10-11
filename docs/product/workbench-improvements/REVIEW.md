# Integrated workbench review · October 11, 2026

This pass continues the native compatibility workbench. The source explorer makes the real reverse-engineering evidence inspectable; navigation, comparison and history expose useful controls without adding a frontend framework or paid component dependency.

## Changes reviewed

- Live 21st.dev workspace-search and Prompt Kit code-block previews inform the grouped native command dialog, exact-copy controls and module source panel. Existing graphite, Uncut typography, state tokens and responsive navigation remain consistent with DESIGN.md. No Copy prompt credits were consumed.
- Original source is fetched only for the selected supported contract. The actual shipped request module has 425 displayed lines and module SHA-256 `561b6159c8ed0df35aa3301de343a7e1506238bde40627f553f1afbe3e83a2ef`; the string entry has 76 displayed lines. Archive identity remains separately visible. REA selection is labelled static inference, not runtime discovery. These are entry modules with shipped dependencies, not the complete app reconstructed.
- Before/current matrices retain their own input, output and mutation evidence. Differences applies to the selected matrix. An eight-path bounded inspector distinguishes missing keys, changed values and input-after behavior; complete outputs remain visible first. Source/input/output copy excludes presentation line numbers and preserves original strings.
- History shows recorded/local/live kind, stored comparison and usage values and a parent link where present. Search is explicitly limited to the latest 100 attempts. Unsupported or partial oracle results have unavailable comparison counts, rather than fabricated failures.
- Every paid repair requires explicit consent. The disclosure binds the selected run; navigation closes it. Cancellation protects candidate acceptance while retaining usage from any response already in flight. Worker submission failures release reservations and leave durable failed attempts.
- GET-only polling recovers with bounded backoff and preserves disclosure state, panel scroll and case-selector focus. Command navigation offers real destinations and saved records. Global shortcut handles capture before nested controls; Escape closes search and restores focus. Enter on Close acts normally rather than running a selected command.

## Verification

The parent independently reviewed the backend diff and reran the previously approved local test command after its final refinement: **19 tests, exit 0, 13.250 seconds**. Actual original-code tests, isolated infinite guest, mutation comparison, invalid submission, idempotency, origin/CSRF/authentication, durable storage, missing consent, unavailable/tampered source, rejected executor and cancelled in-flight response controls passed. Cancellation usage is a mocked 1-call/17-token control, not a claim of real billing.

Ego Browser TaskSpace 4 performed the integrated checks:

| Check | Result and boundary |
| --- | --- |
| Desktop reference | Actual request module/path/hash and 425 code lines; self-only assets; exact copy reported success |
| Desktop comparison | Recorded baseline has 25 differences/80 cases; header substitution shows output and mutation paths; current matrix has no disagreements |
| History | Actual search for recorded evidence returned 2 of the then-loaded 7 attempts, with measured result/call columns |
| Command dialog | Search to history, arrow/Enter navigation, Close with Enter, empty results, Control+K, Escape and restored tab focus passed |
| Local creation | `240c6b324ec6443685b5f84ab0f1359e` reached Mismatch with 2/32 matches and 0 model calls through the real browser form |
| Consent context | Repair disclosure identified that local attempt, unchecked required consent; changing route closed it without any provider call |
| Review | `58ecd9d769e5439b9abbdd5e184894cf` reached Needs review for a random placeholder with both comparison totals unavailable and 0 calls; actual review reason visible |
| Read interruption | Synthetic browser-only GET fault: an existing verified record was temporarily presented as active, the next read failed, and the third read recovered its real Verified state. Backend record unchanged; no worker/model call was started by the fault control |
| Phone layout | 390×844 comparison and original-source screens had scrollWidth 390; 320×760 source and real local mismatch journey had scrollWidth 320; tables/code scroll internally |
| Inspection preservation | Synthetic browser active state followed by the real completed record preserved the open input disclosure and case-selector focus across two GET reads; no backend state changed |
| Tabs and motion | End/ArrowLeft selected and focused Original source; reduced-motion media made button transitions 0 seconds |

Ignored screenshots under `.local/design/`: `workbench-final-desktop.png`, `original-source-desktop.png`, `comparison-mobile.png`, `original-source-mobile.png`. Browser-only fault state and key instrumentation are cleared by the final reload. New durable browser runs are local verification records, not paid repairs.

## Final assessment

All seven declared acceptance gates were reviewed as met, with zero unmet and zero abandoned. The independent audit's substantive findings and three follow-up defects are addressed. Backend behavior remains a single-operator local service and verification covers finite supported Bruno contracts. This pass makes no new live-provider, hosted tracing, public deployment, cloud-resource or hackathon-submission claim.
