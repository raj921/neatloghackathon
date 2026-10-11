# Parity Medic delivery contract

Build a single-operator product for a developer wrapping Bruno's deterministic behavior. Select a supported contract, supply an adapter, verify it, ask the repair agent to fix mismatches, review independently checked results, and download code with a proof manifest. Preserve the original spike.

## Counterarguments resolved before implementation

1. A prettier score is not a product: add durable history, real actions, input editing, failure handling and export.
2. Finite tests can be gamed: keep fresh seeds and original code outside model tools; expose the finite contract and every counterexample. Regression evidence is not a formal proof.
3. Full-app reconstruction is too broad: two real shipped functions, including URL/header/body preparation. Reject unsupported auth, binary, path-parameter and nondeterministic inputs instead of approximating them.
4. An agent may report victory prematurely: only host verification sets verified state. Wrong held-out outputs cannot produce a verified repair download.
5. Duplicate clicks or restarts can burn money: SQLite states and idempotency keys, one worker, bounded calls, explicit interrupted state and manual new attempt.
6. User payloads may hold secrets: synthetic examples; custom JSON verification stays local unless the user chooses repair with clear provider disclosure. Guest processes never inherit keys.
7. Decoration may hide evidence: focused graphite workbench, readable code, measured before/after row, accessible states and purposeful motion.

## Build sequence (Solo)

References and DESIGN.md → verifier/runner → durable API → workbench/journeys → prepared checks → browser/review/operating docs.

Reuse QuickJS, Bruno artifact, REA analysis and Neatlogs SDK. FastAPI handles validation/OpenAPI; SQLite durable state; native browser modules/CSS avoid a frontend build dependency. Model endpoint/model configurable; adapter exports as standalone JavaScript. G1–G6 are acceptance; new checks require inspected approval under the active Unlazy skill.
