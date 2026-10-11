# Gates: minimal workbench integration
OWNS: app/main.py, tests/test_product.py, app/web/index.html, app/web/app.js, app/web/style.css, DESIGN.md, design-references/parity-medic/README.md, docs/product/minimal-ui/REVIEW.md
Scope: complete the requested UI refinement and verify integration.

- [x] G1: Current relevant references inform a concrete updated design direction.
  EVIDENCE: Ego TaskSpace 5 inspected current Component Gallery tabs/icons/disclosures/progress, required typography/theme references, B2B galleries and Linear Docs; concrete updated DESIGN.md and reference README were written before screen implementation.
- [x] G2: Workbench is visually simpler; result distribution and established icons replace repetitive prose.
  EVIDENCE: Parent reviewed .local/design/minimal-final.png against minimal-before.png: one main action, two measured ratio meters, smaller repeated labels, native optional details and aligned panels; all 30 official Phosphor path geometries and original hashes independently matched.
- [x] G3: Existing verification, navigation, inspection and consent controls remain functional in the running app.
  EVIDENCE: Running browser: local verification da202bb973c54d83b55689f86945a0a4 passed 32/32 with zero calls; exact original-source copy payload and actual adapter download, matrix-specific filtering, case focus, keyboard tabs/search, source fingerprints, history and required unchecked repair consent checked. Approved backend suite passed 19 tests. Synthetic browser-only polling kept disclosures open and summary focus; fixture was cleared and real saved state restored.
- [x] G4: Mobile, keyboard, themes and reduced motion retain accessible state and honest data.
  EVIDENCE: 390px comparison/original and 320px consent/review had no document overflow; partial review displayed no meters and two em dashes. Light/dark and loaded Uncut reviewed; reduced-motion control transition measured 0s. Private screenshots named in docs/product/minimal-ui/REVIEW.md.
- [x] G5: Both child deliveries are independently reviewed and consequential findings resolved.
  EVIDENCE: Parent compared every icon path/hash with retained official originals and safe SVG attributes; independent source audit reread the final code and confirmed both freshness-label and disclosure-focus findings resolved. Child ledgers were reread; no unresolved finding. Summary and constraints reconciled against current user request.
