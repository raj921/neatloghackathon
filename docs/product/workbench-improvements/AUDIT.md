# Independent workbench review

Reviewed the current native frontend, FastAPI boundaries, SQLite store, repair worker and pinned original-code harness. This is source inspection; it does not claim browser verification, a paid repair replay or a security audit. Locations below describe the code before this improvement pass and should be rechecked against the integrated change.

## Consequential findings

### P2 · Cancelled attempts can hide measured provider usage

`app/store.py:78–80` rejects every update once a run is cancelled, including metadata. During an in-flight call, `app/service.py:165–168` receives measured usage and attempts to save it before its next cancellation check. That update is discarded. The final trace-delivery update at `app/service.py:142–147` is also discarded. A paid call can therefore finish while the proof and UI continue to show zero calls/tokens and `not_sent`.

Keep cancellation terminal and reject late candidate/source/result acceptance, while recording explicitly allowed measured usage and trace-delivery metadata. Test cancellation inside a mocked provider call, then inspect the durable run: it must remain cancelled, keep its original source, and expose the actual returned usage. Do not retry the paid call.

### P2 · A temporary connection failure permanently stops progress observation

The catch branch in `app/web/app.js:48` announces an error but never schedules another poll. One temporary failure leaves the rendered run active indefinitely until the user reloads, even if the worker has finished. A persistent connection indicator with a Retry control, or bounded GET-only backoff that respects the route version, would restore observation without restarting any repair.

### P2 · Baseline filtering can conceal a new repair regression

`app/web/app.js:63–72` groups and filters only baseline cases. Repaired cases appear in a secondary details panel. If a submitted revision breaks a category that its baseline passed, the Differences filter can exclude that category, even though the run enters Needs review for its current result.

Make the selected inspection phase explicit (baseline/current), or provide a current-result disagreement path. Any summary must say which phase it describes. Host baseline and final comparisons use the same fresh inputs; comparing case IDs is therefore valid for completed repair results.

### P2 · Unsupported inputs are represented as failed measured comparisons

`app/engine.mjs:154` returns `passed: 0`, `total: N` and no cases before any oracle execution for unsupported inputs. An original execution failure can also return a partial case list with a reason (`app/engine.mjs:161`). `app/web/app.js:51–54` accepts the numeric total as enough evidence to display matching-case metrics. Its review captions help, but `0 / N` still suggests a completed comparison.

Use an unmeasured/review presentation when the oracle did not complete. Completed repair mismatches still deserve their real counts. History summaries should use the same distinction rather than convert absent measurement to zero.

### P2 · Modal submission should retain the attempt it disclosed

The repair dialog opens for the current run (`app/web/app.js:90`) but submission reads mutable `currentRun.id` later (`app/web/app.js:99`). Browser Back or an external hash change can change that object while the dialog remains open. Bind the disclosed run ID at opening, or close the dialog on route changes, so consent and submission refer to the same adapter. Keep keyboard command navigation from stacking unrelated native modal dialogs.

## Additional bounded usability risks

- Run navigation assigns `currentRun` before its final route-version check (`app/web/app.js:43–44`). A stale response can leave a global run after another route has rendered. Resolve into a local value, check the version, then assign it; this is particularly useful before adding command navigation.
- Polling rerenders the whole view and restores only tab/case-button focus. It can close open input/output details and remove focus from a case selector. Preserve the selected phase/case and useful disclosure state during GET-only refreshes; a complete page reload is unnecessary.
- History exposes only the latest 100 rows (`app/store.py:70`) while saying “saved attempts.” Label the loaded limit accurately until pagination is implemented. Search should say it searches the displayed records.

## Reference endpoint evidence boundary

The declared `GET /api/v1/reference/{contract}` contract is appropriate if it follows these constraints:

- Use the existing authenticated API boundary and a fixed supported-contract-to-module mapping. Never accept an arbitrary archive or workspace path.
- Call the pinned original harness, which verifies the complete archive SHA-256 before extracting source (`app/engine.mjs:24–29`). The REA selection also checks the selected module identity against the extracted source hash (`app/engine.mjs:172–181`). Unsupported contract names and unavailable/changed artifacts must fail closed.
- Show the selected shipped module's path and source hash separately from the complete artifact hash. The entry module uses shipped dependencies, so its visible source is an inspectable source selection, not a claim that the panel contains every byte executed by the oracle.
- Preserve the distinction between `authority: shipped original source` for extracted code and `graph.authority: static inference` for graph selection. A graph node does not prove runtime coverage or arbitrary feature discovery.
- Keep source read-only and escape it before insertion into the DOM. Do not make a source fetch start a model call, repair or verification job. An explicit retry must only repeat the read.

## Existing controls that should remain intact

Output comparison includes the complete returned value and complete input-after-mutation state, not only a displayed string. The model cannot edit the original or verifier. Export checks the current adapter digest against a completed verification and withholds imported recorded runs until local re-verification. Same-origin writes, CSRF, operator authentication, body limits, static allowlists and the self-only CSP are already material controls; the improvement should preserve them. None of these source observations broadens the finite supported contract into universal Bruno compatibility.

## Integrated source review

The second pass inspected the integrated frontend and backend edits. Runtime/browser observations remain the root agent's responsibility.

### Resolved in the inspected implementation

- Cancellation now admits only measured usage and delivery metadata after entering the terminal state (`app/store.py:90–98`). State/source/result acceptance stays blocked. The backend leaf also records a mocked in-flight-response control; this review did not rerun it.
- Status observation now retries GETs with capped backoff, shows a persistent interruption banner, and respects the route version (`app/web/app.js:55–71`). It does not restart paid work.
- Current/baseline matrix selection makes final repair disagreements independently navigable (`app/web/app.js:105–117`). Reopened repair runs start on the current matrix, and a completed Needs review repair selects its current result.
- Empty unsupported-input matrices display no numeric comparison measurements in the workbench and history. The source review still identifies the partial-oracle case below.
- Repair consent captures the disclosed run ID and includes its title; navigation closes the dialog and invalidates that binding (`app/web/app.js:41–45`, `157`, `166`). The run is assigned only after the final route-version check (`52`).
- Command shortcuts respect another open modal. The palette searches real pages and stored attempts, and its remote fetch only reads history.
- Source loading is lazy, contract-scoped and read-only; the rendered code and graph are escaped. Module and archive hashes remain distinct. The implemented endpoint uses fixed names, authenticated routing and consistency checks (`app/main.py:218–236`).
- Clipboard values retain the original text in a map, rather than extracting decorated code with line numbers. The nearest input/output panel selects its own mapped value. Copy failures announce a manual fallback.
- History labels its latest-100 limit and shows measured results, usage, run kind and parent provenance instead of fabricated fields.

### Follow-up defects reported during this pass

1. **P2 · Keyboard Close can execute a command.** The command-dialog handler at `app/web/app.js:183` intercepts Enter on every focused element. If focus is on Close, it prevents the native button action and invokes the selected command. Limit the custom Enter behavior to the search input and command rows.
2. **P2 · Partial original execution still appears complete.** The `unmeasured` predicate at `app/web/app.js:76` and history projection at `app/store.py:74–79` only detect an empty case list. A Needs review result with fewer executed cases than its total can still display `0 / N`, even though `app/engine.mjs:161` stopped the oracle early. Withhold the full-matrix count, or label an independently computed partial result explicitly.
3. **P2 · Training evidence is described as fresh verification.** `hasCurrentMatrix()` accepts any live run with result cases (`app/web/app.js:34`). The worker initially saves its training result before making model calls; a still-active or failed repair can therefore display the fresh-input captions at `109` and `117` without an independent fresh seed. Reserve that wording for a final comparison identified by the persisted fresh seed, or use “saved comparison inputs” for the initial result.

Lower-impact observation: a status rerender still closes open details and only restores tab/case-button focus. This is bounded to active attempts; completed source and comparison inspection remain stable. Also, the durable cancellation usage arrives only after an in-flight provider response, so reopening the terminal record may be required to see that later measurement.


## Parent integration resolution

The parent fixed the three follow-up defects: Enter is scoped to command input/rows; incomplete oracle matrices with fewer cases than their total are unmeasured in UI and history; a current fresh matrix requires a persisted fresh seed or explicit recorded-request evidence. Browser checks verified Close/Enter, Control+K and Escape. The global shortcut uses capture handling and search Escape explicitly restores focus. Poll refresh now preserves disclosure/scroll state and case-selector focus; a browser-only synthetic-active control retained the open input panel and selector focus across the actual completed record. The previously approved local suite passed 19 tests after the backend refinement. Full runtime evidence and its synthetic boundaries are in REVIEW.md. Cancelled records persist late response usage; reopening retrieves any measurement that arrives after cancellation.
