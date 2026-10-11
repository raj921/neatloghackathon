# Product delivery review · October 11, 2026

## Actual outcome

The durable product acceptance run `2471afc9ae4d4218966329f1d08b5487` improved a deliberately incomplete, plainly labelled sample request adapter from **55/80 to 80/80** on the same fresh inputs across sixteen supported request categories. Another independently selected seed matched **80/80**. Initial training was **22/32**, and the submitted revision matched **32/32**. Three real DeepSeek calls used **28,418 tokens**; measured worker duration was **13.958 seconds**. These are generated inputs within the same categories, not eighty independent integrations or a general reliability rate.

[Full run and independent replay](../../app/evidence/request-live.json), [actual exported adapter](../../app/evidence/request-adapter.mjs), and [hosted Neatlogs readback](../../app/evidence/neatlogs-request-readback.json) are recorded. Trace `7fa65df88286d4f7ff6bc9835c77fb10` is finalized, status OK, eight spans, three LLM calls and four tool calls. The SDK-only delivery flag was captured before its final flush; the record now explicitly points to subsequent remote readback. Hosted estimated cost was $0.0117204; this is not a provider invoice.

The first service integration omitted the spike's explicit non-thinking setting. DeepSeek spent its output budget thinking and produced no adapter. The host refused success. A subsequent diagnostic attempt was stopped to prevent more truncated calls; [diagnostic evidence](../../app/evidence/repair-diagnostic.json) preserves that failure. Explicit non-thinking and required tools fixed the provider handoff. The final successful run is one run; no general success rate is claimed. The prior interpolation spike's 25/50 → 50/50 evidence remains separately intact.

## Review decisions

- Source evidence alone cannot prove behavior. Real downloaded Bruno code supplies expected results in an isolated interpreter; REA records module identity and explicit static limitations.
- A model submission is not success. Independent host comparison decides state and checks output, types, array ordering and full input mutation. A wrong-submission control enters Needs review and cannot unlock export.
- Unknown original behavior must not be guessed. Random/time/Faker, binary, auth workflows, path parameters, gRPC/WebSocket and external request transport are excluded. The random review example stops before a model call.
- Cancellation, repeated operations and restart must not duplicate paid work. Idempotency includes parent and input, cancellation wins over late output, and recovery scans every unfinished record. Work is one process and one worker; horizontal scaling is intentionally absent.
- A configured key is not verified access. Settings says configured; actual acceptance proves this DeepSeek connection. Compatible-provider configuration is implemented but no second provider was called.
- Private data must not leak through presentation or telemetry. Strict same-origin writes, CSRF, body limits, host controls, loopback-client restrictions, sanitized validation, operator cookie access and scoped static assets passed local controls. Guest processes inherit no provider key. These checks do not claim a security audit or tenant isolation.
- Exports need provenance and notices. Adapter download requires a passing current-source digest, includes Bruno's complete MIT notice, and has a companion proof. Recorded evidence must be locally reverified before product export.

## Local and browser evidence

Twelve local tests passed through the user-approved acceptance command. They exercise real original positive/negative comparisons, newly varied interpolation inputs, mutation mismatches, unsupported inputs, guest interruption, durable API/idempotency/export, origin/CSRF/body/path controls, cancellation, restart, operator sessions, remote-client denial and provider tool protocol. A hash-locked Python dependency dry run checked 83 installed packages and would make no changes. A secret-value scan of 88 deliverable files found no configured credential values; no `.env`, `.secrets` or `.local` paths are tracked. Browser-downloaded source matches its proof and includes the full MIT notice; `app/evidence/delivery-review.json` records those checks. The pinned reference preparation confirmed the current archive digest without downloading or executing Bruno.

Ego browser QA used the user's existing TaskSpace 2. At 1440×1000 and 390×844, the workbench and settings were inspected in light/dark themes. Actual UI actions created a 22/33 mismatch using the example input, opened the provider disclosure, cancelled that dialog without a paid call, created a random Needs review attempt, searched history including its empty state, reverified the repaired source at 32/32 with zero model calls, and downloaded both adapter and proof. Keyboard arrows moved evidence tabs; Escape closed the native dialog. Invalid JSON kept the form open with an error. Mobile document width did not exceed the viewport; evidence tabs and history tables intentionally scroll internally.

Screenshots and the browser-downloaded code/proof are private ignored QA artifacts under `.local/design/`. They are not included as synthetic success evidence. The local app presents the real recorded repair clearly as recorded, including its original live ID, actual model usage and finite scope.

## Design and reuse

All 48 saved browser bookmark entries were inventoried; relevant design entries were opened. Refero, MotionSites, ThreeUI, CollectUI and saved motion references informed composition and interactions. Required project reference sites were consulted. Variant's stored authentication error was not treated as design evidence. Six decisions are preserved in `design-references/parity-medic/README.md`; private bookmark details remain ignored.

`DESIGN.md` was written before the product screen implementation. The initial product used sage/white surfaces; the subsequent 21st.dev redesign uses graphite surfaces, warm action accents and sans-serif run headings. Self-hosted OFL Uncut Sans, readable code, actual measurements, accessible status words and reduced-motion handling remain shared constraints. Native frontend modules avoid a build dependency; FastAPI/OpenAPI, SQLite and standalone adapters provide clear replacement boundaries.

## Sponsor and delivery boundaries

Neatlogs records real model/tool activity, and the older spike has a real failing candidate trace. [Entire Graph product search](../../app/evidence/entire-product-search.json) supplied source-review evidence from the working tree; it does not prove a checkpoint or captured coding session. The user reported cfo.ai account setup complete; an actual cfo.ai product business plan has not been verified. AWS/Crustdata credentials remain setup resources and were not added artificially to this product. No public deployment, public repository conversion, social post, demo-video submission or hackathon receipt is claimed.

This is a completed local product with a production foundation and explicit operating boundaries. A multi-user hosted service, arbitrary app feature discovery and broader reference-app support require separate validated work.


## 21st.dev UI redesign review

The follow-up redesign is documented in [its gates](ui-redesign/GATES.md) and the updated design references. Four relevant 21st.dev previews were inspected through Ego Browser: dashboard sidebar, status badges, history table and timeline. Native HTML/CSS adapts their patterns to this product; no React migration, copied component source or paid copy-prompt quota is claimed.

The workbench now leads with the run name and state, one measured result row, and a behavior/code comparison. The navigator filters disagreements and exposes every generated input within each behavior. The initial selection shows an actual disagreement where one exists. Selected items scroll inside their own list without moving the document. JSON tokens are escaped before highlighting; line numbers are hidden from accessibility text. Complete source revisions appear side by side with clear labels. Recorded activity identifies import-time timestamps, local duration is labelled as local verification, and unknown/current counts do not invent results.

Ego checks covered 1440×1000 desktop and 390×844 mobile light/dark screenshots. At 320px, review, settings and history also fit the document width; the history table scrolls within its frame. Native mobile dialogs fit, Escape restores focus, arrow keys change evidence tabs, and reduced motion disables transitions. Invalid JSON preserves the form. History search found the created record and displayed an honest empty state for an unmatched query. Case selection inspected the fifth header-substitution input and its actual repaired output. A matching run produces an empty disagreement view with a route back to all behaviors.

Local UI re-verification `804506d524d9467bb08242d844b7ce83` passed **33/33** using the previously repaired source and one synthetic custom input, with **zero model calls**. Literal `<adapter>` in its title and `<em>literal</em>` in its output remained text, with no injected elements. Browser downloads of adapter/proof preserved source equality, source digest and the full MIT notice. Random review attempt `c83cdc1d06254196bf33535a3ecbebaf` remained Needs review with no adapter download and zero model calls. Its provider disclosure was opened and cancelled; required consent stayed unchecked. No paid repair was submitted for this redesign.

JavaScript syntax and diff whitespace checks passed. Private screenshots/downloads remain ignored under `.local/design/`. The backend, provider configuration, verification engine and existing paid evidence were not changed or rerun. This verifies the redesigned local UI; no public deployment is implied.
