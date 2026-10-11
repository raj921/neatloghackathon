# Parity Medic — compatibility workbench

Read before every screen. References: `design-references/parity-medic/README.md`. Product sequence: inspect disagreement → repair adapter → independent verification → export. Recorded research, local checks, model work and human review are distinct evidence states.

## Visual direction · minimal refinement, October 11

A restrained inspection tool: off-white canvas, a quiet navigation rail, dark primary controls, generous separation between tasks. Keep data dense where it helps comparison; remove repeated narration. One run header and one next action. Before and current matching distributions are visible as measured meter rows. They are separate matrices, not a trend or paired identical inputs. Use short state words beside established icons. Original source, exclusions and provenance stay available through tabs and native disclosures. No promotional hero, fake account avatar, bento marketing cards, gradients, ambient animation or invented icon geometry.

## Typography and tokens

Keep the existing licensed, self-hosted Uncut Sans. Body 14px/1.55, controls 13px/1.4, headings 25px/1.2 at weight 600, secondary 12px. Code ui-monospace 12px/1.75, tabular values and independent scrolling. Use sentence case. Repeated technical metadata belongs in the verification record or an expandable run-details section. No tiny uppercase sentences.

Light default: canvas #fcfcfb, surface #ffffff, raised #f3f3f0, rail #f6f6f3, ink #252723, secondary #6c7068, rule #e5e7e0, primary #292d27 on white. Success #387351 with soft #edf5ef, difference #aa5148 with soft #faf0ed, review #856222 on #faf4e6. Graphite option: canvas #171917, surface #1c1f1c, raised #262a26, rail #141614, ink #e9ece6, secondary #a0a79c, rule #323832, primary #e3e8de with dark ink. Semantic colors remain quiet and always accompany accessible labels and counts. Follow stored theme choice; fresh visitors use light.

4px grid; 8/12/16/24/32 spacing. Rail 192px, main desktop gutters 32px, content max-width 1240px. Run header aligns its action to the right. Secondary navigation and comparison start directly below the result summary. Controls 6px radius, panels 8px, 1px boundaries only where sections need separation. No panel shadow. Shadows only for dialogs and notices.

## Icons and visual signals

Use pinned original Phosphor Bold SVG assets from the official core repository. Self-host a sprite and preserve MIT attribution/source manifest in `app/web/icons/`. ViewBox 256, icons 16–18px; brand uses the original checks symbol, not a fabricated mark. Navigation keeps words. Search, copy, close and theme may be icon-only with explicit accessible name and hover/focus tooltip. Touch target remains 44px. Do not replace essential consent or errors with icons.

Result meters show exact measured passed/total counts. Never label these task progress; use meter semantics. Unknown/partial matrices show an em dash and a visible review state. Small behavior strips summarize that category's actual matching inputs. Never animate saved measurements. No runtime icon package, external fonts or shader library.

## Screens and behavior

Workbench: short run name, state, contract and recorded/live/local label. One next action. Compact measured before/current meters; calls/tokens/duration stay accessible in run details. Five concise evidence tabs with established icons. Comparison matrix switch remains explicit: Before vs Fresh verification. Category navigator shows names, matching distribution and count. Selected case, input disclosure, aligned adapter/reference outputs and exact differing paths. Scope disclosure retains exclusions and finite evidence limits. Recorded repair must explain that local reverification is required for export.

History: searchable actual runs with compact rows, stored states/results/usage and honest latest-100 limit. Evidence: source → execution → trace is a three-step diagram with short labels and expandable technical limits, not a claim all dependencies were captured. Settings: plain separated rows for readiness, source, access and sponsors; no invented online status. New verification: name + contract first; custom source/input in optional advanced disclosure, automatically opened when editing or loading review case. Paid repair keeps provider/call ceiling/data destination and mandatory consent visible.

## States, access and responsiveness

All controls keep 44px targets and visible 3px focus. Tabs support arrows/Home/End. Native dialogs support Escape and focus restoration. Important failed/review/connection states remain explicit. Polling preserves open details and inspection scroll without stealing focus. No auto-started repair. Changed run closes stale repair consent.

Below 1000px rail becomes compact top navigation. Below 760px result meters remain legible, cases become a bounded two-column grid and outputs stack. At 390px and 320px there is no document-level horizontal overflow; tabs/table scroll within their containers. Short nav labels keep all destinations available. Colors/opacity transitions 140ms; reduced-motion disables transitions/worker animation. Case distributions remain static.

## Reference decisions

Component Gallery's tabs, icon and native disclosure guidance inform progressive inspection and conventional controls. Its progress examples establish the distinction between completion progress and a saved measurement; use meters for our ratios. Uncut supplies existing readable type. Tweakcn Mono/Modern Minimal inform neutral semantic tokens. Design for B2B/Minimal Gallery inform hierarchy, not decorative landing-page elements. Paper Shaders, DialKit and Number Flow were revisited: none improves this saved evidence workflow, so retain native CSS and static measured numbers. Existing 21st.dev references remain historical context; the orange/card-heavy direction is superseded by this quieter pass.
