# UI redesign gates · 21st.dev

OWNS: app/web/**, DESIGN.md, design-references/parity-medic/**, docs/product/ui-redesign/**, docs/product/REVIEW.md, docs/product/PLAN.md

Scope: redesign the existing local Parity Medic frontend. Preserve real repair/verification behavior, recorded evidence boundaries and provider consent. No model calls are needed for design validation.

- [x] G1: Inspect relevant current 21st.dev components and project references in Ego Browser; document the chosen implementation decisions before changing screens.
  EVIDENCE: Ego TaskSpace 3 inspected rendered sidebar/status/table/timeline components and required resources. DESIGN.md and six reference decisions updated before implementation. The original ledger was written as docs/product/UI-REDESIGN.md before edits and moved here at completion.
- [x] G2: Deliver a cohesive workbench, comparison, history, evidence, settings and dialog design; all controls remain functional and measurements come from actual run data.
  EVIDENCE: Graphite/warm-accent shell, real measured result row, escaped numbered JSON, per-input selection, disagreement filter and whole-file revisions. History, evidence, settings and native dialogs share the same tokens. No framework or component dependency added.
- [x] G3: Inspect desktop/mobile and light/dark; verify keyboard, filtering, local creation/review, source/proof and downloads in the browser.
  EVIDENCE: Ego desktop 1440x1000 and mobile 390x844 light/dark visual review; 320px review/settings/history widths do not overflow. Arrow-key tabs, Escape/focus restoration, filter/empty state, case-70 selection, expanded input/repaired output, invalid JSON and history match/empty states checked. Local run 804506d524d9467bb08242d844b7ce83 passed 33/33 with zero model calls. Random review c83cdc1d06254196bf33535a3ecbebaf blocks adapter export. Both browser downloads saved and checked against proof source/digest and MIT notice. Provider disclosure opened and cancelled with required unchecked consent.
- [x] G4: Confirm safe escaped rendering, JavaScript syntax, clean diff and private repository scope. No new paid repair check.
  EVIDENCE: Literal HTML in title and output stayed text with zero injected elements; node syntax check and git diff whitespace check exit 0. GitHub reports raj921/neatloghackathon PRIVATE; existing codex/parity-medic-product branch retained. Only scoped frontend/design/review files are staged; private screenshots, downloads, credentials and local database stay ignored.

Counter-design: remove promotional serif headlines, repeated success slogans and disconnected score cards. Build an instrument-like workspace where state, discrepancies, source and proof are the hierarchy. Prefer adapted native components over adding a React toolchain to this working app.
