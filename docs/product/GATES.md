# Gates: Parity Medic product

OWNS: app/**, tests/**, docs/product/**, design-references/parity-medic/**, DESIGN.md

Scope: a complete single-operator local product for supported Bruno deterministic interpolation and request preparation. Durable runs, real bounded repair, explicit review, evidence export and polished responsive UI. Public SaaS deployment and hackathon posting are separate actions.

- [x] G1: Saved design bookmarks are inventoried and relevant references inform a written design system before screens are built.
  EVIDENCE: 48 bookmarks inventoried through rendered Ego bookmark manager; relevant saved sites opened; six reference decisions and DESIGN.md written before app/web creation. Private snapshots are ignored.

- [x] G2: Local verifier and API controls reject bad repairs, unsupported requests, hostile origins, unauthorized access and duplicate paid work; runs survive restart.
  CWD: ../..
  CHECK: .venv/bin/python -m unittest discover -s tests -v
  EXPECT: /^OK$/m
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/Users/rajkumar/neatloghackathon; path=9fe063a82109/51 entries; EXPECT=matched; output-sha256=952829afa2ea49d599651d5b5292266d8dda2821cf65a1184e6c76dabc18fdce; output-bytes=2128

- [x] G3: A real request-workflow repair completes through the durable service and passes independent fresh cases, with honest remote tracing status.
  CWD: ../..
  CHECK: .venv/bin/python scripts/product_live_check.py
  EXPECT: PRODUCT_LIVE_VERIFIED
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/Users/rajkumar/neatloghackathon; path=9fe063a82109/51 entries; EXPECT=matched; output-sha256=b354c2fab9bf68588e88d522dd3b4c4c82f2c9f487daa6e078a03b706ac8b61b; output-bytes=547

- [x] G4: Browser inspection verifies desktop/mobile, create, inspect, repair or review, history, settings, error handling and download journeys.
  EVIDENCE: docs/product/REVIEW.md records actual Ego desktop/mobile light/dark journeys, mismatch/review creation, 32/32 local recheck, both browser downloads and keyboard/error behavior; ignored screenshots under .local/design.

- [x] G5: Reproducible setup, pinned dependencies, architecture, review, API documentation and operating guidance exist; credentials and private bookmark state are excluded.
  EVIDENCE: OPERATING.md, ARCHITECTURE.md, REVIEW.md, hash-locked Python/npm dependencies, pinned reference bootstrap and authenticated OpenAPI; dependency dry-run checks 83 installed packages with no changes. Secret scan is recorded in REVIEW.md.

- [x] G6: Final outcome and sponsor claims match current evidence; unperformed deployment, cfo.ai plan and submission are explicit.
  EVIDENCE: README and REVIEW match request-live.json and independent replay (55/80 → 80/80, 3 calls, 28418 tokens); hosted readback finalized 8 spans/3 LLM; Entire working-tree search is labelled. cfo.ai plan/public deployment/submission explicitly unperformed; scope remains finite local product.
