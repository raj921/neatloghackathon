# neatHack inspiration research

Researched October 10, 2026. Scope: product inspiration and project selection only. No product code, paid tool calls, infrastructure, public posts, or account changes were made during this research.

## Recommendation

Start by considering **Contract Medic**: an agent that notices an order-data import has become wrong, investigates the upstream change, repairs the importer in a sandbox, and proves the recovered data is correct before proposing the fix.

The strongest alternatives are **Order Rescue**, for a visible commerce workflow, and **FreshProof**, for research using our existing Crustdata access. These are working concept names, not researched trademarks. The shortlist is our synthesis of observed mechanisms, not a claim that these concepts are globally new or likely to win.

This is a broad scan of **25 distinct products across six discovery surfaces**: Product Hunt, YC, BetaList, Uneed, Hacker News, and GitHub. Some products appear on more than one surface and are counted once. It is not an exhaustive inventory of every launch site. Listings and maker descriptions establish what products claim to do; they do not establish customer demand, actual reliability, or independent commercial success. We did not sign up for or run these products.

## How the supplied expert advice changes selection

The user supplied Parth's August 19, 2026 article about finding hackathon ideas. Its authorship, participation counts, and award claims were not independently checked. The useful selection method is:

1. Begin with real products, demos, and problems, then combine mechanisms rather than asking for an unrestricted list of AI ideas.
2. Make the organiser's technology visible in achieving and improving the result. For this event, an observable failure, investigation, and verified rerun is a strong way to use Neatlogs.
3. Explain the product in one sentence and reveal the useful outcome within the first minute of the demo.
4. Look for a timely change in what agents can do. A recent listing is an inspiration signal, not proof that an idea is early.
5. Use domain knowledge we can actually defend. No assumed access to hospitals, banks, fleets, or enterprise customer data.
6. Match the event's actual theme, rather than importing the criteria of a different hackathon.
7. Keep the complete task narrow enough to finish. Extra agents, 3D scenes, and integrations must earn their place.
8. Treat execution quality and experimentation as valuable outcomes; no research can promise a prize.

The [official neatHack brief](https://neatlogs.com/hackathon) calls for a substantial task completed by an agent or agent team. It requires Neatlogs, Entire, and cfo.ai, evidence of improvements and failures, a public repository, and a demo of at most three minutes. Judging: agent 30%, sponsor use 25%, demo 20%, building in public 15%, usefulness/originality 10%. This makes a clear result and checkable recovery more useful to us than architectural size.

## Recent product landscape

Dates below mean exactly what the cited surface exposes. A YC batch is not a launch date. A BetaList feature or Uneed launch is a listing date. Relative HN/PH timestamps are observations made on October 10, not independently exported release dates. Older 2026 products remain explicitly marked as broader context.

| ID | Product and primary/listing source | Observed recency | Mechanism worth studying; what to avoid copying |
| --- | --- | --- | --- |
| S01 | [Tector](https://www.producthunt.com/products/tector) | PH says “Launching today”; company info says 2026. | Check a research deck's claims against collected evidence, including contradictions. Borrow claim-level accountability; avoid a general research validator with the same pitch. Product site required sign-in. |
| S02 | [IrisGo](https://www.producthunt.com/products/irisgo-public-beta), [product site](https://irisgo.ai/solopreneur) | PH's latest launch badge: October 7, 2026; earlier beta April 16. | Demonstrate a task once and reuse the workflow. Borrow the understandable show/execute/result interaction; avoid building an entire desktop operating system. |
| S03 | [Monid](https://www.producthunt.com/products/monid), [product site](https://monid.ai/) | PH launch award references September 2, 2026; three launches listed. | Agents discover and invoke tools at runtime with payment consolidated. Borrow tool choice and explicit budgets; do not introduce paid-tool spending into our demo without a concrete need. |
| S04 | [Agent Relay](https://www.ycombinator.com/companies/agent-relay) | YC Fall 2026; founded 2026. | Shared agent messaging, session history, checked/resumable workflows, and intervention. Borrow recovery with visible state; avoid making another general coordination platform. |
| S05 | [Pentagon](https://www.ycombinator.com/companies/pentagon) | YC Spring 2026, broader 2026 context. | A workspace for agents and people coordinating work. Borrow a readable account of who did what and why; avoid a large organisation simulator before proving one task. |
| S06 | [OneCLI](https://www.ycombinator.com/companies/onecli), [repository](https://github.com/onecli/onecli) | YC Summer 2026; repository inspected. | Sandboxed agents, policy enforcement outside the model, protected credentials, and sensitive-action approvals. Borrow authority boundaries; do not claim our prototype has enterprise isolation merely because it has an approval button. |
| S07 | [Pango](https://www.ycombinator.com/companies/pango) | YC Summer 2026. | Agents operate the work after checkout: deliveries, returns, refunds, and claims across tools. Borrow a concrete completed business operation; avoid cloning its broad e-commerce OS. Its numerical customer/performance claims are not used as verified evidence. |
| S08 | [TrueMile](https://www.ycombinator.com/companies/truemile) | YC Fall 2026; founded 2026. | Agents coordinate loads, routes, driver schedules, and fuel stops. Borrow replanning under operational constraints; avoid physical fleet execution, which we cannot validate here. The current company profile describes operating its own fleet. |
| S09 | [Lance](https://www.ycombinator.com/companies/lance) | YC Winter 2026, broader 2026 context. | Hotel agents turn requests into multi-step operational work using existing software. Borrow the request-to-fulfilled-task loop; avoid requiring a real hotel system or voice stack on the critical path. |
| S10 | [Terminal Use](https://www.ycombinator.com/companies/terminal-use) | YC Winter 2026; founded 2026, broader context. | Redesign one operational process around agents, existing systems, and people at control points. Borrow starting from a workflow's failure points rather than choosing a framework first. |
| S11 | [Alkera AI](https://www.ycombinator.com/companies/alkera-ai) | YC Summer 2026; founded 2026. | Data agents use history, lineage, team knowledge, and specialised tools. Borrow context-aware investigation and safe data work; avoid a broad warehouse/IDE platform. |
| S12 | [HyperProbe](https://www.ycombinator.com/companies/hyperprobe) | YC Summer 2026; founded 2026. | Gather runtime evidence at the failure rather than guessing from inadequate logs. Borrow evidence-directed diagnosis; do not duplicate Neatlogs or promise live process probing we have not built. |
| S13 | [Canary](https://www.ycombinator.com/companies/canary) | YC Winter 2026, broader context. | Source-aware QA connects developer intent with broken user flows. Borrow checks tied to a user outcome; general autonomous QA is already directly represented in this scan. |
| S14 | [CoArena](https://www.ycombinator.com/companies/coarena) | YC Summer 2026; launch copy says released two weeks earlier, but the post's absolute date was not exposed. | Compare agents on the same real task and judge their actual outputs. Borrow a fair before/after comparison and task-specific oracle; avoid presenting a small demo corpus as a universal benchmark. |
| S15 | [TensorTest](https://www.ycombinator.com/companies/tensortest) | YC Winter 2026; current profile describes a pivot from Ritivel. | A valid video file can still fail the client's creative brief. Borrow verification against intent, not just technical validity. Its reported benchmark results are vendor-reported and not reproduced here. |
| S16 | [Financial Datasets](https://www.ycombinator.com/companies/financial-datasets) | YC Summer 2026; founded 2024, an older product anchor. | Structured, searchable source data for research agents. Borrow provenance and data-specific tools; no trading or investment-advice agent is recommended. Access would require separate commercial arrangements. |
| S17 | [Clerk.AI](https://betalist.com/startups/clerk-ai) | BetaList featured October 8, 2026. | Collect bank statements, match receipts, flag omissions, and prepare an accountant handoff. Borrow assembling a complete evidence packet; avoid real banking access. Direct product redirect could not be retrieved, so this is a maker listing, not a tested service. |
| S18 | [Mainbrella](https://betalist.com/startups/mainbrella) | BetaList featured October 6, 2026. | Isolated workspaces with idempotent operations and generation checks. Borrow predictable execution and stale-state detection; no need to buy a sandbox platform before establishing a need. Direct product redirect was inaccessible. |
| S19 | [Save Genie](https://betalist.com/startups/save-genie) | BetaList featured October 9, 2026. | Monitor prices/restocks and make a changed condition visible. Borrow observable event triggers; alerts alone would leave our hackathon task incomplete. Direct product redirect was inaccessible. |
| S20 | [Reeve](https://www.uneed.best/tool/reeve), [product site](https://reeve.page/supabase-backups) | Uneed launch date October 10, 2026. | Verify backup contents and preserve a safety copy before restore. Borrow proving recoverability; avoid building a general backup service or using production databases for the demo. |
| S21 | [Since.dev / Grant](https://since.dev/), [Uneed review](https://www.uneed.best/tool/since-dev/reviews) | Product page shows changes since September 26 and latest recorded October 3, 2026; this is activity, not a verified founding date. | Specialists monitor CI, costs, runtime, security, and dependencies with evidence. One September 22 reviewer describes silent crawler failures despite HTTP 200. That is one anecdote, not demand validation. |
| S22 | [Pocketty](https://pocketty.app/), [HN October 9 archive](https://news.ycombinator.com/front?day=2026-10-09) | Present in the October 9, 2026 HN archive. | Notify the user when an agent is blocked, return to the exact session, and inspect changes. Borrow a precise human handoff; avoid building an iOS SSH app for this event. |
| S23 | [Big Arrow on the Screen](https://github.com/franzenzenhofer/big-arrow-on-the-screen), [Show HN](https://news.ycombinator.com/show) | Show HN displayed 21 hours ago when checked October 10. | A CLI/skill lets an agent point at a specific human action without stealing input focus. Borrow visible guidance and an easy-to-understand demo. It is a Mac tool, not our planned cross-platform dependency. |
| S24 | [Rutter](https://ruttermemory.com/), [Show HN](https://news.ycombinator.com/show) | Show HN displayed two hours ago when checked October 10. | Recall prior decisions and the notes an AI session cited. Borrow a link from a current action to previous evidence; avoid adding a general memory service. Product extraction was limited and a later fetch failed. |
| S25 | [iimos](https://github.com/yanglongyun/iimos), [Show HN](https://news.ycombinator.com/show) | Show HN displayed two hours ago when checked October 10; repository inspected. | A local app modifies itself, with boot snapshots and rollback described in its README. Borrow sandboxed change and visible recovery; avoid unrestricted self-modification. README demonstrations were not reproduced. |

GitHub Trending could not be fetched. Specific linked repositories were inspected instead; no trending rank, star-based popularity score, or adoption ranking is claimed. X was represented by the supplied article; no logged-in X feed was inspected. Reddit/Indie Hackers search results were used only as possible discovery leads, not as verified product facts.

## What this scan suggests

These are interpretations of this sample, not measurements of the whole market:

- Agent coordination already has direct examples in Agent Relay, Pentagon, and OneCLI. A general “agent team dashboard” needs a much sharper contribution.
- Evidence and verification recur across Tector, Alkera, HyperProbe, Canary, CoArena, TensorTest, and Reeve. A useful result needs an independent definition of correctness.
- Pango, Lance, and TrueMile ground agents in completed operations, rather than conversational features. This gives us a natural beginning and end for a demo.
- Pocketty and Big Arrow make a blocked agent understandable. A well-designed human handoff can be part of a substantial autonomous task.
- Since.dev's single reviewer example suggests a valuable test case: software can return success while the business result becomes wrong. It does not prove a market opportunity by itself.

## Six directions to discuss

All time estimates below are rough engineering judgments for a small prototype, not commitments. They assume one configured model provider, available local tooling, seeded data, and no enterprise integration onboarding. A model key has not yet been selected. None of the proposed workflows has been implemented or measured.

### A. Contract Medic — recommended for technical depth and controllable verification

**One sentence:** “When an order-data import silently goes wrong, this agent finds the change, repairs the importer, and proves the business numbers are right.”

- **User / impact hypothesis:** A small commerce/data team maintaining supplier or order feeds. Avoid silently missing records or incorrect totals. Real willingness to pay remains untested.
- **Inspiration:** Alkera's data context (S11), Since.dev's dependency evidence and reviewer example (S21), Reeve's verified recovery (S20), iimos's bounded rollback (S25).
- **Agent task and decisions:** Observe a violated data contract; inspect the actual response, pagination, schema and previous successful run; choose a hypothesis and a diagnostic test; propose a parser patch in an isolated branch; rerun import; verify the complete output; produce a reviewed fix and evidence packet. Ambiguous field meanings require clarification rather than invented values.
- **Distinct contribution to pursue:** One feed's silent business corruption, with record/total invariants and a repair verified on held-out payloads. Alkera and Since.dev already overlap; this is a narrow emphasis, not a global novelty claim.
- **First-minute demo:** The API returns 200 but the dashboard's order total is wrong. Open the violated contract, watch the agent inspect the changed payload, then see the repaired import pass checks. The underlying change is deliberately injected and labelled as such.
- **Failure/recovery:** Kill the worker after a page is imported; resume from saved state without duplicating records. Keep unknown semantics in a review state.
- **Metric / oracle:** Expected record IDs, required fields, duplicate IDs, and totals calculated independently from controlled source records; repair success on fresh payloads; model cost and latency. No claimed improvement until baseline and repaired runs actually exist.
- **Sponsor contribution:** Neatlogs shows the failing import and investigation, then the verified rerun. Entire preserves the coding change and its context. cfo.ai models per-feed pricing, job costs, support effort and margin using labelled assumptions and measured run cost when available.
- **Small complete version / ceiling:** One local HTTP feed, one importer, one business contract, one repair branch, one persistent run ledger. Roughly 14–22 engineering hours. No warehouse, generic ETL builder, automatic production deployment, or cross-tenant platform.

### B. Order Rescue — strongest visible business workflow

**One sentence:** “Give it a failed order, and it finds a policy-compliant exchange or refund, carries it out in the test system, and proves the customer was handled once.”

- **User / impact hypothesis:** A small e-commerce operations team handling delivery failures and exchanges. Fewer unresolved cases and less duplicate work; no commercial impact has been measured.
- **Inspiration:** Pango's post-checkout operations (S07), TrueMile's constrained coordination (S08), Lance's request-to-fulfilment loop (S09), OneCLI's approval boundary (S06).
- **Agent task and decisions:** Read the order, policy, stock and customer's intent; choose exchange, refund, alternative or escalation; verify stock and limits; perform the approved action; check resulting order/inventory/action records; assemble a customer response for review.
- **Distinct contribution to pursue:** Prove recovery when an action commits but its response is lost, or stock changes during execution. This is closely adjacent to Pango; the reliability demonstration must be substantial, not just a different name.
- **First-minute demo:** An exchange fails after stock changes. The agent replans and completes the valid alternative. The action ledger proves a timeout did not issue two refunds or two replacements.
- **Failure/recovery:** Timeout after commit; query operation status, reconcile observed state and resume. Only retry using the backend's documented semantics; a new operation key must not silently create a duplicate.
- **Metric / oracle:** Resolution correctness against policy, duplicate side effects, stock consistency, actual escalation rate over a small labelled case set, cost per resolved case.
- **Sponsor contribution:** Neatlogs pinpoints the ambiguous timeout and before/after retry behaviour; Entire captures the corrected tool adapter; cfo.ai compares per-case pricing, support cost and model/infra cost.
- **Small complete version / ceiling:** One order backend, one exchange/refund policy and seeded inventory; genuine model tool choices against an executable local system. Roughly 16–24 hours. This would be a working controlled prototype, not a live Shopify/carrier/payment integration. Such integrations require separate access and validation.

### C. FreshProof — easiest path to using our existing data credits

**One sentence:** “It finds companies matching your business question and delivers a shortlist whose important claims are sourced, dated, and rechecked.”

- **User / impact hypothesis:** A founder or analyst selecting potential partners/vendors. Reduce decisions based on stale or misidentified company information; value remains a hypothesis.
- **Inspiration:** Tector's claim validation (S01), Financial Datasets' source-oriented data tools (S16), Rutter's decision evidence (S24), CoArena's task comparison (S14).
- **Agent task and decisions:** Convert a question into criteria; search companies; resolve entities by domain/identifier; enrich records; fetch supporting sources; investigate contradictions; revise the search when results fail the criteria; deliver a shortlist with verified, uncertain and excluded claims.
- **Distinct contribution to pursue:** Freshness and entity identity for one concrete business decision, with revalidation of decision-critical claims. General sourced research and deck verification are already represented by Tector.
- **First-minute demo:** A plausible-looking company has the same name as the intended vendor. The agent discovers the mismatch and removes it; the final shortlist links to the right entities and evidence dates.
- **Failure/recovery:** Rate limit or a source that changed; checkpoint partial evidence, retry within a fixed budget, and mark unresolved claims instead of completing them by guesswork.
- **Metric / oracle:** Entity match accuracy on labelled cases, proportion of material claims with supporting source/date, false validation rate, contradictions left unresolved, credits/model cost per shortlist. Crustdata responses are evidence, not automatic guarantees of truth or freshness.
- **Sponsor contribution:** Neatlogs exposes the mistaken entity/tool call and revised run. Entire captures the matching/validation correction. cfo.ai models pricing per researched brief and data-credit costs. Crustdata has a natural additional role.
- **Small complete version / ceiling:** One question, three to five companies, one shortlist and a fixed credit/tool-call budget. Roughly 10–18 hours. [Crustdata's CLI](https://docs.crustdata.com/for-agents/cli) documents company identify/search/enrich and web search; this project's active key and balance were verified during setup, but research queries have not been run here. No automated outreach.

### D. Approval Guide — strongest human-agent interaction experiment

**One sentence:** “An agent prepares a vendor's onboarding record and asks you only for the exact authority or missing evidence it needs to finish.”

- **User / impact hypothesis:** A small operations team onboarding suppliers. Reduce confusing handoffs while retaining control over commitments.
- **Inspiration:** Big Arrow (S23), Pocketty (S22), OneCLI (S06), Terminal Use (S10).
- **Agent task and decisions:** Gather company identity and provided documents, check a defined policy, prepare the vendor record, identify a missing field or approval, pause with exact context, resume after the response, and verify the stored record matches the approved proposal.
- **Distinct contribution to pursue:** A complete onboarding task with evidence-aware, resumable handoffs. A notification overlay alone is insufficient; vendors' claims cannot substitute for verified documents.
- **Demo / failure / metric:** Wrong company identifier or expired evidence triggers a specific request; approval arrives and the task resumes once. Measure correct completion, unnecessary interruptions, and unauthorised writes using a labelled task set.
- **Sponsor contribution:** Neatlogs exposes the blocked step and resumption; Entire captures the policy/checkpoint implementation; cfo.ai models onboarding-service pricing and review labour.
- **Scope / feasibility:** One supplied document pack and local vendor registry, no live procurement purchase or third-party login bypass. Roughly 14–22 hours; browser and document integration is an additional risk. Native permission/MFA prompts remain human actions.

### E. Brief-to-Verified-Edit — strongest creative output

**One sentence:** “Give it your footage and a short ad brief, and it edits a video, checks the required content, and repairs the edit when the brief is missed.”

- **User / impact hypothesis:** A small creative/marketing team making constrained clips. Reduce deliverables that are technically valid but miss requirements.
- **Inspiration:** TensorTest (S15), IrisGo's clear demonstrated workflow (S02), CoArena's output judging (S14).
- **Agent task and decisions:** Inspect/transcribe permitted footage; select scenes; produce an edit; check duration, required shots and captions; revise the parts that violate the brief; export the result and verification report.
- **Distinct contribution to pursue:** One explicit brief and traceable corrections. No claim that a programmatic verifier measures professional taste; subjective quality requires human review.
- **Demo / failure / metric:** The first edit omits a required product shot or has an inaccurate caption; the verifier finds it and the agent revises the export. Measure explicit-constraint compliance, subtitle accuracy on labelled speech, duration, export integrity and human preference separately.
- **Sponsor contribution:** Neatlogs shows scene/tool choices and revision cost; Entire captures the verification/editor correction; cfo.ai models per-video economics including review effort.
- **Scope / feasibility:** Three user-owned clips, one short brief, one export. Roughly 18–28 hours. Editing/transcription/model access is not established for this repository. Cut if a real tool round trip cannot be established quickly; no new generative-video dependency on the critical path.

### F. Journey Judge — strongest adversarial verification

**One sentence:** “It tests whether your agent really completed an expense-preparation task, then finds the smallest failure that explains a false success.”

- **User / impact hypothesis:** A team shipping an administrative agent. Catch incomplete or incorrect output that the agent called successful.
- **Inspiration:** Canary (S13), CoArena (S14), Clerk.AI (S17), HyperProbe's evidence-directed diagnosis (S12).
- **Agent task and decisions:** Turn a stated task into outcome assertions, prepare a controlled variation, run the target agent, inspect generated files/records, reduce a failing case, and produce a reproducible failure plus a verified rerun after a targeted fix.
- **Distinct contribution to pursue:** One expense packet's completeness and absence of duplicate/conflicting evidence, not a general QA or benchmark platform. The overlap with Canary and CoArena is substantial.
- **Demo / failure / metric:** The target agent reports success but two same-amount transactions share the wrong receipt. The independent check finds the error, isolates the counterexample, and the repaired agent assembles the correct packet.
- **Sponsor contribution:** Neatlogs provides the causal execution trail and comparative runs; Entire captures the repair context; cfo.ai models pricing per verified workflow and verification overhead.
- **Scope / feasibility:** One folder of synthetic labelled invoices/transactions and one target agent. Roughly 14–24 hours. No bank login or tax advice. A second agent is justified only if it independently performs adaptive test-case search; deterministic output checks remain outside the model.

## Comparative judgment

These are relative editorial judgments, not numerical winning probabilities or customer evidence.

| Direction | Demo clarity | Engineering depth | Access risk | Direct competitor overlap | Decision |
| --- | --- | --- | --- | --- | --- |
| Contract Medic | Strong: wrong data becomes correct | Strong: diagnosis, repair, independent checks, replay | Low with a local feed | Medium/high: Alkera, Since.dev | First technical option |
| Order Rescue | Strong: failed order becomes resolved | Strong: changing state and duplicate prevention | Low locally; high for real integrations | High: Pango | First business workflow option |
| FreshProof | Strong if one wrong entity is visible | Medium/strong: adaptive search and evidence checks | Medium: credits, sources and freshness | High: Tector/general research tools | Best existing-data option |
| Approval Guide | Strong if the handoff completes the task | Medium/strong: state, approval and identity | Medium/high for real portals | Medium/high: OneCLI and agent workspaces | Explore if interaction is the main ambition |
| Brief-to-Verified-Edit | Strong: immediately visible output | Strong, but tool work is substantial | High until editing/model access is verified | Medium/high: creative agents | Ambitious reserve |
| Journey Judge | Strong when false success is obvious | Strong: independent verification and counterexamples | Low with local documents | High: Canary and CoArena | Technical alternative, needs a sharper wedge |

Deprioritise a general agent builder, broad multi-agent dashboard, generic sales chatbot, universal research assistant, autonomous trading agent, and a new on-call/observability platform for this event. This judgment is specific to our time, sources and sponsor fit; those categories are not inherently bad businesses. Avoid a 3D “agent city” until a useful underlying workflow exists; the supplied article is inspiration, not evidence that the same visual concept will fit this brief.

## What “industry standards” should mean for this build

For us it should mean observable properties, not a production-ready label:

- Validate tool inputs and observed outputs against a task-specific contract. A model saying “done” is not the completion check.
- Store progress durably and make retries reconcile actual state. Operation keys and their retention/parameter semantics belong to the backend contract; do not promise universal exactly-once execution. [Stripe's first-party idempotency documentation](https://docs.stripe.com/api/idempotent_requests) is a concrete example of why these details matter, not a planned Stripe integration.
- Keep policy, permissions, and approval enforcement outside the model, with minimal tool authority and secret-safe traces. [OWASP's Excessive Agency guidance](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/) supports these boundaries.
- Make run IDs, source/evidence versions, input versions, tool results, costs and final outcomes inspectable. Distinguish the controlled failure injection from an organically discovered defect.
- Demonstrate happy path, recoverable failure, and a case that must stop for review. Run a comparison on fresh cases instead of tuning only the recorded demo.
- Begin with one decision-making agent and deterministic validators. Add a separate worker only when an independently verifiable task needs it. [Anthropic's agent-building guidance](https://www.anthropic.com/engineering/building-effective-agents) supports increasing complexity only as needed; it also flags its older examples as dated.

No compliance certification, security audit, customer deployment, or production-readiness assessment has been performed. These properties are proposed acceptance criteria.

## Feasibility against our actual setup

| Dependency | Established now | What still needs a real check |
| --- | --- | --- |
| Neatlogs | SDK probe and readback passed during setup. | Real project traces, an actual failure investigation, and before/after application runs. Existing evidence is synthetic setup evidence. |
| Entire | CLI installed and enabled. | Hooks require approval; latest status reported 11 pending hooks and zero checkpoints. First genuine coding checkpoint remains required. GitHub hosted identity connection remains unconfirmed. |
| cfo.ai | User confirmed setup completion. | Actual business-plan output and credit/billing state have not been independently verified. |
| Crustdata | Key and 5,200-credit balance verified during setup. | Candidate-specific API calls, data coverage and credit cost. No research credits spent in this pass. |
| AWS | Separate event profile verified, $25 shared allowance allocated. | Any application deployment. us-east-1 only; EC2, Lambda, IAM roles and load balancers only. No Bedrock. Do not assume S3/RDS or other services are included. |
| Model provider | None selected for this project. | A working key, one real tool-use round trip, latency and cost. AWS credits do not resolve this dependency. |
| Data | Public sources inspected; controlled records can be authored later. | Target workflow access and a user's actual problem. No real customer interviews or private business data collected. |

Local SQLite/file state and a local task backend are reasonable prototype options; selecting or implementing the stack is deferred until a direction is chosen. A local executable task with seeded records can prove real agent behaviour, but it does not prove a real merchant, bank, warehouse or hotel integration.

## Skills discovery

Completed `npx skills find 'market research'` and `npx skills find 'competitive analysis'`. No new skills were installed. CLI installation counts were not used as quality/security evidence.

| Skill | Why it may help next | Limit and status |
| --- | --- | --- |
| [customer-research](https://www.skills.sh/coreyhaines31/marketingskills/customer-research) | Analyse interviews, support material, and community language; label confidence and sample bias. | Public summary inspected. We have no real customer interviews yet. Not installed or executed. |
| [competitor-profiling](https://www.skills.sh/coreyhaines31/marketingskills/competitor-profiling) | Compare positioning, pages, pricing and features consistently once a direction is chosen. | Public summary inspected; it also uses SEO/market tools such as DataForSEO, whose access is not established. Not installed or executed. |
| [Firecrawl market research](https://skills.sh/firecrawl/firecrawl-workflows/firecrawl-market-research) | Potential broader automated collection if the manual source pass becomes too slow. | Found by CLI; its page could not be retrieved here, so its full instructions were not audited. Firecrawl access is not established. Not installed or executed. |

Optional later installation, if selected: `npx skills add coreyhaines31/marketingskills@customer-research` or `npx skills add coreyhaines31/marketingskills@competitor-profiling`. Existing browsing and note-taking were sufficient for this pass. Ponytail ultra governs future scope; Unlazy's research gates record the completed source and feasibility review.

## Next decision, with a concrete kill test

Choose among Contract Medic, Order Rescue, and FreshProof based on which problem the team understands best. Then, before designing screens or expanding architecture:

1. Confirm the problem with one actual user or a documented issue. If we cannot explain the painful failure in one sentence, narrow the task.
2. Establish a real model/tool call and a task-specific verifier. If the verifier only asks another LLM whether the output looks right, strengthen it or change the task.
3. Run one successful task and one recoverable failure. If we cannot show the difference quickly, cut scope.
4. Preserve the actual Neatlogs traces and Entire checkpoint, then model the costs in cfo.ai. Do not replace missing execution evidence with a generated screenshot.

The next pass should validate one direction. This research does not authorise building a product idea automatically, changing the repository to public, sending outreach, or spending sponsor/model credits.
