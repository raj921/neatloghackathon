# Independent minimal-interface audit

Scope: source inspection of `app/web/index.html`, `app/web/app.js`, `app/web/style.css` and `DESIGN.md`. No browser observations, runtime checks, provider calls or backend changes were made by this leaf. Source locations below describe the interface at the start of this pass; function names remain the stable references when integration shifts lines.

## Pass 1 — user journey and reduction

The primary journey is to understand a disagreement, inspect an exact input, repair deliberately, and inspect independently verified output. The first screen should therefore prioritize the run state, measured agreement, one next action and the comparison. It currently introduces that journey repeatedly: source tags, description, run metadata, four three-line metric cells, uppercase action metadata and a scope paragraph (`sourceInfo`, `renderRun`, app.js 35, 76–84). Those labels compete with the result rather than clarify the current decision.

Recommended reduction:

- Use one aligned title/status/action row and a subordinate source/version label. Recorded evidence must retain its visible provenance so it is not mistaken for a current local verification.
- Make matching and differing proportions visible with a simple measured bar or case marks. Retain the exact numerator and denominator in text. Before/current counts describe separate input matrices; do not draw a line that implies the same individual cases changed over time.
- Put IDs, timestamp, usage, duration and technical scope in a native details disclosure. They should remain reachable without leaving the run. Keep active state and interruption/review/error notices visible.
- Reduce explanatory paragraphs in comparison output panels. Keep file/object labels, status glyphs, exact output, mutation status and copy controls. Detailed limitations belong in expandable scope and the Evidence page.
- Replace hand-drawn navigation icons and character substitutes with the original licensed icon assets. Keep visible navigation words; use icon-only controls for familiar copy, search and theme actions with explicit accessible names.
- Optional adapter/input fields in the new-verification dialog can be grouped under an advanced disclosure. Keep the name and contract visible, preserve entered values on errors, and keep the synthetic-input guidance reachable beside the optional input.

## Pass 2 — product semantics and evidence

The existing source already protects several important distinctions. A minimalist redesign should carry these into its visuals, not delete them.

| Constraint | Existing source evidence | Redesign requirement |
| --- | --- | --- |
| Baseline and current inputs differ | `currentCases`, `hasCurrentMatrix`, `comparison`, app.js 33–34, 107–121 | Keep an explicit matrix switch and phase-specific labels. Do not pair by case ID alone. |
| Partial/unsupported oracle execution is not a failed full matrix | `renderRun` unmeasured predicate and `comparison` partial notice, app.js 78, 112 | Render no full-matrix percentage, count or progress bar when the oracle stopped early. Preserve the review reason and only expose executed inputs. |
| Recorded repair needs local re-verification before export | `renderRun` action branches and recorded wording, app.js 79–80 | Retain Recorded provenance and the Reverify action; do not show imported evidence as an exportable current result. |
| Reference selection and execution are separate authorities | `original`, `proof`, `renderEvidence`, app.js 129, 138, 147 | Preserve module/archive hashes and the static-selection explanation in progressive detail. The displayed entry module is not a claim that every dependency's source is visible. |
| Full files are not a minimal code diff | `patch`, app.js 137 | Before/after source panels must remain labelled complete files or revisions. |
| Model work needs deliberate consent | repair form in index.html; app.js 44–45, 161, 170 | Keep provider, limits, data recipients, unchecked required checkbox and explicit start action readable. Never turn Repair into a silent one-click paid action. |
| Cancellation can finish an in-flight call | `cancel` branch, app.js 162 | Preserve the explanation that acceptance stops while measured usage may still arrive. |
| Finite local scope, no network transport | `renderRun`, `renderEvidence`, app.js 84, 147 | Keep the limitation accessible, particularly if replacing the visible scope paragraph. Do not imply universal Bruno compatibility. |

## Pass 3 — interaction defect hunt and preservation checklist

No new source-confirmed implementation defect is raised against the existing interface in this pass. The following are the concrete regression traps to inspect during integration:

1. **Copy the undecorated value.** `codeView` stores the original text in `copyValues`; the handler resolves the nearest `.output-panel,.input-panel` and its `data-copy-key` (app.js 21–26, 151–152). Keep those structures or adapt the handler together. Copy must not include line numbers, headings, syntax spans or the neighboring panel. Re-rendering clears/rebuilds the map, including original-source loading and phase/filter changes.
2. **Filter the selected matrix.** `comparison` groups `currentCases`; Differences applies only to the displayed phase (app.js 107–121). Switching phase resets category/sample selection but does not silently reset the filter (153). A verified current matrix with Differences selected should show a truthful empty state and an All option.
3. **Keep the exact case selected and reachable.** Category selection resets sample; the sample selector rerenders and restores its own focus (155–156, 167). `scrollCaseIntoView` keeps the active category within the bounded list (87). Use actual category and sample counts, not decorative marks that imply unexecuted cases passed.
4. **Keep mutation comparisons.** A matching output can still disagree on input mutation. `differenceRows` compares execution error, output, complete input-after state and mutation flags; it limits display to the first eight paths (90–105). The input-after disclosure is conditionally shown when either side mutates (121). Preserve these exact-path and input-after views; label any eight-path truncation honestly.
5. **Bind consent to the disclosed run.** Opening Repair resets consent and captures `repairRunId`; changing routes closes the dialog and clears that binding (44–45, 161, 170). Do not read a mutable current run during later submission. Commands must not stack on top of another native modal.
6. **Preserve keyboard operation.** Tabs use roving tab stops plus ArrowLeft/Right/Home/End (84, 148). Matrix/filter/category controls restore focus after their DOM replacement (153–156). Native dialog Escape and explicit Close restore trigger focus (36–37, 189–190). Search Enter is intercepted only on its input or command rows, so Enter on Close stays native (187). Icon changes must not remove these hooks.
7. **Preserve inspection during real polling.** `captureInspection` and `restoreInspection` currently cover only `#tab-content details` and code/case/difference scroll positions (73–74). If metadata or scope moves into a disclosure outside that container, extend preservation to it; otherwise an active-run update will close it. Focus preservation currently recognizes tab/case data attributes and element IDs (62–64).
8. **Retry observation without replaying work.** Poll failures show a persistent interruption notice and perform GET-only capped-backoff reads tied to the route version (55–71). Reducing words must leave a recognizable interruption state and the saved comparison available. Do not present fabricated progress percentages.
9. **Keep history provenance and scope.** History labels the latest-100 limit and exposes recorded/local/live kind, parent lineage and real usage (139–144). Search is over those loaded records. Progressive detail can shorten rows but must retain these distinctions, especially zero measured calls versus no usage recorded.
10. **Keep source retries read-only.** Original source is loaded lazily by fixed contract and escaped before insertion; retry only reloads that reference (123–134, 159). Replacing its button icon must not invoke verification or repair.

## Pass 4 — visual and accessibility polish

- Use shared tokens and one type scale rather than shrinking helper text further. The current stylesheet uses numerous 9–11px helpers/statuses (`metric`, `case`, footer and responsive rules); deletion/grouping is more legible than smaller type.
- Prefer fewer container borders and one dominant comparison surface. Align all panel headings and icon controls to the same baseline; maintain the established 4px spacing grid.
- Every icon-only control needs an accessible name describing its action and target. Decorative sprite SVGs should be hidden from assistive technology. State colors need a glyph and readable state text or an equivalent programmatic label.
- Preserve 44px touch targets and visible focus (`style.css` 78–80, button rules). A visually smaller icon can remain centered in a full-size hit area.
- Keep tab and table overflow internal on small screens. The 390px acceptance check should include long run names, hash strings and a differing JSON payload; 320px dialogs should preserve all consent text and actions.
- Static counts should remain static. Use motion only for actual worker state, with `prefers-reduced-motion` honored (`style.css` 1145–1150). A progress-like visual should show measured match distribution, not pretend to estimate worker completion.
- Review dark and light themes separately. Decorative icon opacity and newly introduced small segmented bars need enough contrast in both token sets.

## Acceptance boundary

This leaf completes the source-based opportunity/constraint audit. The parent owns implementation, rendered visual judgment, interaction checks and evidence. A later integrated source reread can confirm preservation before the parent closes the browser gates.

## Integrated source reread

Reviewed the implemented minimal pass against the ten preservation traps. This remains source evidence; rendered checks belong to the parent.

Preserved in the inspected implementation:

- `hasMeasurement` suppresses the full-matrix number and meter when Needs review has fewer executed cases than its total. The native meter has passed/total semantics and an accessible measured label, not worker progress (`app.js:76–77`).
- Recorded provenance stays visible in the source strip and recorded note; imported evidence offers Reverify rather than adapter export (`app.js:36,82–86`).
- Matrix switching still requires real fresh evidence, and Differences still groups the selected matrix. The empty disagreement view names its current/baseline input count (`app.js:34–35,111–124`).
- Exact-copy maps, input/output panel wrappers, mutation disclosure and first-eight differing paths remain intact (`app.js:22–27,94–109,124,155–156`). Icons do not replace the underlying copy values.
- New metadata/scope disclosures are included in the open-state capture by stable details IDs (`app.js:74–75,85,88`).
- Custom source/input fields are optional and open automatically when editing or loading the review example. Their values remain in the form after submission errors. Repair retains its readable provider/call ceiling, required unchecked consent, bound run ID and route invalidation (`index.html` dialogs; `app.js:40,45–46,165,168,173–174`).
- Navigation/state text, icon accessible names, tab key handling, command-modal Enter scoping, internal code/tab overflow and reduced-motion rules remain present (`app.js:13,21,152,191–194`; `style.css:7,20–22,32,41,65`).
- Reference identity remains available under Source fingerprints; static selection and independent behavioral execution remain distinguished. Before/after adapter files retain their complete-file wording (`app.js:132,140`).

### Resolved P2 — training comparison relabelled as fresh verification

`renderRun` labels the result meter “Fresh verification” for every live or recorded kind (`app.js:81,85`). Unlike the comparison matrix switch, this label does not check `hasCurrentMatrix`. The worker initially stores `baseline=result, result=result` before it calls the model (`app/service.py:122`); its fresh seed arrives only with the final host comparison (`app/service.py:220–221`). A still-repairing, cancelled or failed live attempt without a fresh seed can therefore show its measured training result as fresh verification.

Use the same persisted fresh-evidence guard for the result-meter wording. Before that evidence exists, label the result “Saved comparison” or “Current comparison”; do not infer freshness from the live run kind. The actual numerator/denominator and partial-result suppression can remain unchanged.

### Resolved P2 — polling loses focus on the new disclosure controls

Polling restores focus by a tab data attribute, category data attribute or element ID (`app.js:63–65`). The new run-details and scope-details summaries have no ID (`app.js:85,88`). A user can focus one with the keyboard, open it, then receive a worker update. The details open state survives, but replacing the main DOM removes the focused summary and nothing restores it.

Give the summaries stable IDs so the existing focus restoration can select them, or capture a stable enclosing-details/summary focus key. The same strategy can cover original fingerprints and activity-details summaries. Keep focus restoration scoped to a focused element inside the rerendered main; unrelated modal focus should not be moved.

No additional source-confirmed regression was found in the requested meter/partial, copy, consent, keyboard-command or responsive-rule review. The two findings above were sent directly to the implementing parent for correction.

### Final integrated outcome

Both reported findings are resolved in the final inspected source. The result meter uses `hasCurrentMatrix(r)` before saying “Fresh verification”; other results say “Current comparison” or “Recorded result” (`app.js:85`). The run/scope summaries now have stable `run-details-toggle` and `scope-details-toggle` IDs, matching the existing polling `focusId` restoration (`app.js:63–65,85,88`). Their details open-state preservation remains intact.

The responsive hide rule now targets `.sample-control .case-outcome`; the Settings missing-key warning remains outside that selector (`style.css:60,63`, `app.js:149`). The server's fixed asset allowlist adds only the sprite and checks favicon, and the existing path-boundary test source checks these assets plus rejection of the icon manifest (`app/main.py:312`, `tests/test_product.py:262–269`). This leaf inspected the checks; it did not execute them.

No unresolved source finding remains from this audit. Browser rendering, actual focus behavior and the local suite remain the parent's evidence responsibilities. No implementation edits, runtime checks or provider calls were performed by this leaf.
