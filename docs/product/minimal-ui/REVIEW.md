# Minimal workbench refinement · October 11, 2026

The workbench now prioritizes the run, measured agreement and the next action. Repeated introductory prose, safety captions and metric cards have been removed from the default view. Neutral controls, quiet semantic colors, a shared type scale and aligned code panels replace the earlier orange presentation. Source identity, scope, event metadata and custom inputs remain accessible through native disclosures.

## Design and assets

Current Component Gallery tab, icon, disclosure and progress examples were inspected in Ego Browser, alongside the required design references and Linear Docs. Decisions are recorded in `DESIGN.md` and `design-references/parity-medic/README.md`. No new framework or runtime library was installed.

All UI icons use the official Phosphor Bold paths pinned to commit `2b75f3ad12b420c9504ef05df8d2564a28f8500e`. Thirty retained originals, their hashes and the MIT license are in `app/web/icons/`. Parent inspection compared every sprite path with its retained original, checked the hashes and inspected the permitted SVG elements/attributes. Only the sprite and checks favicon were added to the server's explicit asset allowlist. Neighboring provenance files and Python paths remain unavailable through `/assets`.

## Verification

- Existing approved test suite: **19 passed**, final run 10.795 seconds. Includes real local verification/export, consent, cancellation, partial oracle results, authenticated paths and the expanded static-asset boundary. No paid provider calls.
- Browser local request verification `da202bb973c54d83b55689f86945a0a4`: **32/32**, zero model calls. Actual exported adapter downloaded to the ignored local evidence folder.
- Recorded request evidence still shows **55/80 before**, **80/80 fresh verification**, three saved calls and 28,418 saved tokens. Those are existing recorded measurements, not a new model run.
- Baseline Differences selected five categories and displayed concrete output/input-after paths. Switching to the fresh matrix truthfully showed zero differences; All restored the matching case navigator. Selecting the third input preserved selector focus.
- Original request entry module displayed **425 lines**, the exact path and accessible module/archive fingerprints. Original-source copying produced the exact source bytes in an intercepted clipboard-write payload; the operating-system clipboard was left unchanged.
- Tabs handled End/Home with focus on Record/Comparison. Command search opened History by keyboard; history filtering matched actual loaded rows. Editing opened the optional source/input section with the adapter populated. Invalid JSON preserved the typed value and showed the error.
- At **390px**, the comparison and original source had no document-level horizontal overflow. At **320px**, repair consent fit the viewport and remained required, unchecked and invalid until consent. Escape closed the dialog and restored Repair focus; the underlying run retained zero model calls.
- Unsupported/random review evidence showed **Needs review**, two em dashes and **no meters**. Light and dark rendered correctly; self-hosted Uncut loaded. Reduced-motion emulation yielded a zero-second control transition.
- A **browser-only synthetic GET status fixture** exercised polling without changing a server run or starting model work. The training result stayed labelled Current comparison, not fresh. Re-rendering preserved the open run/scope disclosures and focused summary. Instrumentation was removed, the page reloaded to the real Mismatch record, and media/device overrides were cleared.

The independent source audit found two regressions during implementation: freshness was labelled too early, and new summary focus could be lost during polling. Both were fixed and independently reread. The audit is in `AUDIT.md`.

Private rendered evidence remains ignored under `.local/design/`: `minimal-before.png`, `minimal-final.png`, `minimal-final-dark.png`, `minimal-differences.png`, `minimal-local-verified-mobile.png`, `minimal-consent-320.png`, and `minimal-source-mobile.png`. Temporary interaction scripts were not committed.

## Scope

This is a local UI refinement with a narrow static-serving integration change. The agent, provider and verifier behavior are unchanged. No new paid repair, cloud resource, public deployment or hackathon submission is claimed. Five integration gates and three child gates were manually reviewed: eight met, zero unmet, zero abandoned. These manual gates describe visual and interaction evidence; the separate executed suite supplies automated backend verification.
