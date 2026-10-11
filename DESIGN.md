# Parity Medic — compatibility workbench

Read before every screen. References: `design-references/parity-medic/README.md`. Product sequence: disagreement → inspect original behavior → repair adapter → independent verification → export. Recorded research, local checks, model work and human review are distinct evidence states.

## Visual direction · October 11 redesign

A graphite developer workspace, informed by the rendered 21st.dev dashboard sidebar, status badge, invoice table and product timeline. Compact navigation frames the actual comparison; orange identifies actions and selected controls. Sans-serif run names replace promotional display headlines. Measured results share one horizontal instrument row. No decorative gradients, simulated progress, fake metrics or unrelated illustrations. Adapt these patterns using the existing native HTML/CSS/JavaScript stack; do not imply third-party component source was installed.

## Typography and tokens

Self-hosted Uncut Sans, OFL license preserved, 400–700, font-display swap. Body 14px/1.55; headings 28px/1.2, 24px mobile; panel titles 13px/1.4; helpers 12px. Code ui-monospace 12px/1.7 with line numbers and restrained JSON highlighting. All result and usage numbers are tabular; render saved measurements directly rather than replaying a count-up.

Dark default: canvas #111214, surface #191a1d, raised #202125, rail #0d0e10, ink #eeedf0, secondary #a5a4ad, rule #303136, accent #ff965b with #21160e button text. Success #8ad5b0 on #1b3028; error #f2a093 on #362522; review #e9c881 on #302a1f. Light option: canvas #f5f4f1, surface #ffffff, raised #efeeeb, rail #eeede9, ink #242428, secondary #64646d, rule #dddcd8, accent #ad4218 with white button text. Success #216b47, error #a53b2a, review #795416. State always includes an icon or word, never color alone.

4px grid; 8/12/16/24/32 spacing. Rail 216px; desktop gutters 32px; mobile 16px. Frame fills available width up to 1800px. Control radius 6px, panel 10px; subtle 1px boundaries. Shadows only for dialogs/toast. Main title and status on one row; actual scope directly below. Navigation has real destinations, no invented organization switcher or account avatar.

## Screens and behavior

Workbench: source/version breadcrumb, run name/status, before/current or before/after counts, usage, main action, evidence tabs, behavior navigator and before/reference code. Filter all behaviors or disagreements, select each actual generated case within a behavior, inspect original input and repaired output. Saved records are labelled; export eligibility follows the server. Code panels scroll internally and wrap long JSON strings. The source view labels complete before/after files rather than claiming a minimal diff.

History: search actual saved runs, state, contract and date; IDs subordinate to names. Evidence: actual source chain and supported/excluded scope. Settings: provider readiness and sponsor evidence, never credentials. Native dialogs keep input labels, optional source/JSON and synthetic-input guidance. Paid repair disclosure and mandatory consent remain explicit before submitting.

44px interactive targets, 3px visible keyboard focus, tab arrow/Home/End navigation, native Escape and focus restoration. 150ms color/opacity transitions; no looping decorative animation. Real worker states alone may animate, disabled under prefers-reduced-motion. Errors preserve inputs. The selected case remains visible while inspecting results.

Below 1000px navigation becomes a compact top row; below 760px comparison panels stack and behavior selector becomes a bounded scrolling grid. Below 550px metric row becomes two columns; topbar remains legible, dialog fits 320px, table scrolls internally. No document-level horizontal overflow at 390px.

## Resource decisions

Uncut supplies readable typography; tweakcn's neutral/graphite theme approach informs consistent semantic tokens. Dark Design was inspected for dark hierarchy. Paper Shaders add no explanatory value to code comparisons and are omitted. DialKit's live tuning model informed browser spacing review; no production tuning overlay. Number Flow's accessible value changes are useful for live counters, but this app mostly displays immutable saved results, so no animation dependency is added.
