# Decision: Parity Medic

Research and local feasibility work, October 11, 2026. This replaces the current recommendation, while preserving the Recall Relay experiment on its branch. It is not a guarantee of a prize or a finished submission.

**An agent repairs an integration by asking the original application what the correct behavior is.**

The user knows developer tools and agent reliability. The strongest available evidence is now a working adapter-repair loop against a downloaded application's code. A real first-pass model implementation matched 25/50 fresh inputs. The agent inspected recovered source, tested two revisions, and submitted an implementation matching 50/50. This is a useful improvement over the earlier Recall Relay comparison, where the baseline already passed.

## The concrete developer job

A team wraps an existing application's behavior for an agent or automation. The wrapper succeeds on the happy path but subtly changes variable resolution, serialization or state transitions. Parity Medic finds a concrete disagreement, retrieves the relevant evidence, repairs the wrapper and reruns a comparison against the original.

For this spike the application is Bruno, and the contract is its `interpolateString(str, options)` function. Bruno itself was not broken or modified. The failures were in a new model-generated adapter. Future product scope should remain one supported Bruno request workflow before expanding to other applications.

The memorable demo is two outputs from the same input, followed by the repaired output and an inspectable proof. The product should sell compatibility verification for developer integrations, not a claim that every application can instantly become an agent.

## What REA actually contributes

Downloaded and inspected [morluto/rea](https://github.com/morluto/rea), pinned to `21650455a9c90a26e725c3505a3c17054cc4516c`. The locally installed runtime is `rea-agents@6.4.0` under the ignored research directory. No global MCP setup, client restart or native disassembler was required for the JavaScript experiment.

The actual source separates CLI/MCP entrypoints, shared application workflows, artifact readers, isolated source analysis and domain contracts. `JavaScriptApplicationService` validates inputs, reconstructs an artifact, checks graph bindings, then creates Evidence. `JavaScriptArtifactFiles` verifies bytes against the earlier inventory; it rejects entries that changed. These mechanisms are visible in the [pinned service](https://github.com/morluto/rea/blob/21650455a9c90a26e725c3505a3c17054cc4516c/src/application/javascript/JavaScriptApplicationService.ts) and [artifact reader](https://github.com/morluto/rea/blob/21650455a9c90a26e725c3505a3c17054cc4516c/src/artifacts/javascript/JavaScriptArtifactFiles.ts).

The important borrowed ideas are artifact identity, source-linked findings and explicit unresolved observations. A static edge is a lead to investigate, not evidence that a workflow ran. REA's own [JavaScript workflow documentation](https://github.com/morluto/rea/blob/21650455a9c90a26e725c3505a3c17054cc4516c/docs/javascript-application-workflows.md) also distinguishes static comparison from behavioral probes.

Locally, REA analyzed a **seven-file, host-selected request-related slice**, parsing six JavaScript files with zero parse failures and recording 342 findings. It observed 25 main IPC handlers in that slice. These counts do not describe the entire app. One large file exceeded a semantic-result budget; the summary retains that limitation. See [REA summary](evidence/rea-summary.json) and [artifact manifest](evidence/bruno-manifest.json).

The repair agent receives two host-selected recovered source files. It does not yet autonomously locate arbitrary features through REA's graph. Automatic graph-to-probe selection remains product work; the current experiment must not be presented as “drop any app and get a verified tool.”

## Downloaded reference app and observed proof

[Bruno 4.2.1](https://github.com/usebruno/bruno/releases/tag/v4.2.1), published September 30, was downloaded as its official macOS arm64 ZIP. Its published SHA-256 matched `0573c46a7049c4def8a55a78edf6fe6202cae2ea6c8475da8cfc819408455ae9`. The extracted `app.asar` hash is `fe9b4c89660ac3f1291707746f76b9b5850edda368a5e0250055687ab02ec767`.

The reference was not installed into Applications or launched as a desktop app. The experiment runs its shipped interpolation module, bundled common library and lodash inside isolated QuickJS. A vacant `crypto.subtle` object permits an unrelated bundled capability reference to initialize; no crypto implementation is supplied. Random, clock-dependent and cryptographic behavior is outside this deterministic comparison contract.

| Measurement | Observed result |
| --- | --- |
| First-pass training inputs | 10/20 match |
| First repair | 18/20 match; literal dotted key still wrong |
| Second repair / submission | 20/20 match |
| First-pass fresh inputs | 25/50 match |
| Repaired fresh inputs | 50/50 match |
| Provider | Real DeepSeek `deepseek-flash` |
| Model calls / tokens | 5 / 21,275 |
| Local elapsed time | 20.509 seconds |
| Neatlogs readback | Finalized, 13 spans, 5 LLM calls, 21,275 tokens |

The fresh set uses different names and values across the **same ten categories** as training. Some categories repeat constant shapes. These are not fifty independent real-world integrations or unseen behavior classes. One successful run does not establish a general success rate.

No expected output table was hand-written: the downloaded code produces the reference outputs. Host controls additionally compare identical original code, reject a known wrong adapter, inspect absent guest host bindings and interrupt an infinite loop. The model can read evidence and submit candidate code through three allowlisted tools; it cannot edit the oracle or generator through those tools. This is tool-level separation, not a claim that a local operating-system user cannot edit the files.

The separate random-UUID probe observes two different original outputs and returns `needs_semantic_oracle`. It shows why exact equality is inadequate for that category. The model-generated adapter explicitly does not implement Bruno's Faker placeholders; it is an experimental deterministic subset, not a deployable general replacement.

Records: [model run](evidence/model-run.json), [controls and unsupported probe](evidence/self-check.json), [Neatlogs export](evidence/neatlogs-export.json), [server-read counterexample](evidence/neatlogs-counterexample.json). The repaired code is [exported with attribution](../../prototypes/rea-parity/repaired-adapter.js), alongside Bruno's MIT license.

## Current competition, with sample boundaries

Read the latest rendered event announcements and general discussion, plus the product community's show-and-tell messages. This sample does not cover every entrant, historical thread or submission.

| Observation | Current evidence | Effect on our choice |
| --- | --- | --- |
| FirstRun, October 11 at 12:30–12:31 IST | [Discord post](https://discord.com/channels/1528866100207419472/1555500199772823613/1558736140146835466), [live site](https://firstrun.atharvashah.com/), [repo](https://github.com/HighnessAtharva/firstrun) | Quickstart execution, repair and fresh-container proof already have a direct entrant. Avoid this task. Site observed; its reported run totals were not independently replayed. |
| benana, October 11 at 11:44 IST | [Discord](https://discord.com/channels/1528866100207419472/1555500199772823613/1558724505638010960), [builder's X post](https://x.com/xmang01/status/2109164255052533888) read in browser | A Minecraft plugin-writing, playing and fixing loop is already being built. A game alone is not a uniqueness strategy. |
| GBA harness, October 11 at 12:30 IST | [Event message](https://discord.com/channels/1528866100207419472/1554463484752830504/1558735994168021072) | Another game-oriented agent harness; execution quality remains unverified. |
| Medic and Upshift, earlier scan | [Medic](https://x.com/David63694631/status/2108835553751810278), [Upshift](https://x.com/harsh_g_0108/status/2108839957788004679) | Repair remains crowded. Our externally grounded oracle is the distinction to demonstrate, not the word “Medic.” These earlier descriptions are retained from docs/DIFFERENTIATION.md, not newly replayed today. |

Current announcements also provide a shared $20 LiteLLM budget per checked-in team. AWS does not include Bedrock. DeepSeek remains our working provider; no LiteLLM key was claimed during this research. The organizer announced TheVibeFounder's session live at 12:03 IST; that was an observation at research time, not a claim it remains live now.

## Fresh inspiration and counter-research

The [October 9](https://www.producthunt.com/leaderboard/daily/2026/10/9) and [October 10](https://www.producthunt.com/leaderboard/daily/2026/10/10) Product Hunt listings were inspected alongside primary product pages. A listing may be a product update; it is not evidence of adoption or a product's first release. Earlier research remains in docs/INSPIRATION.md.

| Source | Useful mechanism | Decision |
| --- | --- | --- |
| [OpenPilot](https://openpilot.in), on the October 9 Product Hunt list | Existing desktop tools, compatible model providers, explicit approvals | Borrow narrow executable capabilities; do not build another general desktop assistant. |
| [OpenVids](https://openvids.ai), same listing | Agent actions produce a visible inspectable artifact | Show the changed output first. Video-editor scope is too large for this build. |
| [OpenCharm](https://www.producthunt.com/products/opencharm), same listing | A convenient interface around an existing coding agent | Interface convenience is secondary to a verifiable developer outcome. |
| [Archal, YC S26](https://www.ycombinator.com/companies/archal) | Stateful API environments for agents and evaluation | Generic API digital-twin/sandbox factories already overlap a current YC company. Reject that broad pitch. |
| [Canary, YC W26](https://www.ycombinator.com/companies/canary) | Code-aware QA and user journeys | Generic AI QA is crowded; choose adapter behavior against a shipped artifact. Vendor metrics are not our measurements. |
| [Prized, YC S26](https://www.ycombinator.com/companies/prized) | Durable development environments and persistent agent work | Useful future hosting pattern; not a reason to build a cloud-devbox product now. |
| [Hypercubic, YC F25](https://www.ycombinator.com/companies/hypercubic) | Agents operate existing specialist systems | Supports the legacy-integration problem; we lack a real mainframe environment. |
| [Frigade founder's Show HN](https://news.ycombinator.com/item?id=48847834), [product workflow](https://frigade.com/how-it-works) | Learn authenticated app workflows and expose actions | Direct overlap with “reverse engineer an app into tools.” Our proposed deliverable is an adapter counterexample and finite parity proof, not universal app-to-agent generation. |
| [SkillWeaver](https://github.com/OSU-NLP-Group/SkillWeaver) | Exploration and reusable skill synthesis | Generic self-improving skill generation is prior art. |
| [mcp-drift](https://github.com/trungpro5398/mcp-drift) | Tool-schema and description drift detection | Useful adjacent competitor. Our probe executes behavior rather than relying solely on declared schemas. |
| [DynamicMCPBench, July 2026](https://arxiv.org/abs/2607.20531) | Verify effects rather than final prose | Supports effect-based evaluation; do not call this principle our invention. |
| [Haven, 2026](https://atlas.cs.brown.edu/pdf/haven:euromlsys:2026.pdf) | Static tool-side-effect analysis and constrained execution | A generic tool-permission scanner is also established work. We use constrained execution as infrastructure. |
| [ReProAgent, July 2026](https://arxiv.org/abs/2607.09123), [Sentry Seer](https://blog.sentry.io/introducing-seer-agent/) | Reproduction and debugging from evidence | Automated reproducer/debugger is also prior art. Narrow the customer task and show actual external behavior. |

The supplied Parth article is a useful heuristic: combine mechanisms, understand a real problem, make sponsor technology useful and show the result quickly. Its author's reported wins are not independently verified, and it cannot predict neatHack judging. Our combination is REA's evidence discipline + an external original-code oracle + a constrained repair loop.

The requested Find Skills search returned protocol-reverse-engineering and spec-miner among its closest results: [protocol skill](https://skills.sh/wshobson/agents/protocol-reverse-engineering), [spec miner](https://skills.sh/jeffallan/claude-skills/spec-miner). No additional skill installation was necessary for this implementation.

## Sponsors and judging fit

The [official brief](https://neatlogs.com/hackathon) weights the agent 30%, sponsor use 25%, demo 20%, building in public 15%, and usefulness/originality 10%. Neatlogs, Entire and cfo.ai are required. Optional sponsors should support the user job rather than decorate the architecture.

| Requirement | Evidence or concrete remaining work |
| --- | --- |
| Agent | Real inspection → counterexample → repair → test → submission; finite supported contract. |
| Neatlogs | Finalized trace `c405bfc5853fc69ad8cd142c99c8cccc`. Public API readback verified the 18/20 intermediate failure, five calls and final workflow. Displayed cost is a Neatlogs estimate, not a provider invoice. |
| Entire | Installed `entire-graph@v0.4.0` in an ignored project-local plugin directory. Used ranked search and caller lookup to review the probe boundary. [Search](evidence/entire-search.json) and [Python probe callers](evidence/entire-probe-callers.json) are real working-tree outputs; they have explicit completeness limits. This is not a checkpoint. Codex hook trust remains outstanding. |
| cfo.ai | Account setup was user-confirmed earlier. A product-specific business plan has not been created in cfo.ai. Use measured run usage, label price/revenue assumptions, and model pricing, costs, revenue and runway. |
| Demo | Read-only viewer shows real 25/50 → 50/50 evidence. It does not run a new model call. A final ≤3 minute video must cover all three required tools. |
| Public build | No new X or Discord messages were posted. Existing repo is private. Public-repository and #neatHack sharing requirements remain submission work. |
| AWS / Crustdata | Optional. AWS may host the bounded worker later; Crustdata is unnecessary for this developer workflow. Neither was used by this spike. |

Entire's lookup did not resolve the `context` symbol in the `.mjs` file. The review continued with the parsed Python `probe` callers and direct source inspection; graph search output alone is not sandbox verification.

## Build boundary and next implementation

This research pass delivered a working narrow proof and an actual evidence viewer, not a production service. Preserve the current result as a regression case. The next scope is **one Bruno request workflow**: select a request-related path from the graph, compare the adapter's prepared request against the original on fresh collections, then produce a replayable counterexample and repaired artifact. Keep network destinations restricted to a local test server until that comparison is trustworthy.

Before calling it a strong complete entry: add at least one new behavior class or second independently selected function, exercise the declared unsupported path in the agent's decision loop, create the cfo.ai plan, make the submission evidence accessible, and record a sponsor-complete demo. Keep the first minute on the real mismatch and result. This is a bounded delivery plan, not a claim those features have been implemented.

The planned close remains October 12 around 11:55 PM IST; the final cutoff is announced on Discord. Prefer finishing the demonstrated workflow and sponsor evidence over another broad idea search.
