# Direction review after the Discord overlap

Research date: October 10, 2026. Proposal only: no pivot is selected, no product code is written, and no retail or identity system is connected.

## What changed

The Discord scan exposed a close event neighbour: [Medic](https://x.com/David63694631/status/2108835553751810278) describes finding a failed agent step, patching configuration, rerunning, and checking unseen tasks. [Upshift](https://x.com/harsh_g_0108/status/2108839957788004679) describes repairing code after version changes. These are builder descriptions, not tested results.

Contract Medic's supplier-import focus remains a difference, but repair plus held-out verification is no longer enough to explain its distinction. A more unusual name or more agents would not change the task. We should compare a different user job before starting implementation. Do not infer that every entrant has the same idea from this small Discord sample.

The supplied expert article suggests combining mechanisms, choosing a task we understand, making the result visible early, and giving sponsors a meaningful role. The [event brief](https://neatlogs.com/hackathon) prioritises completed agent work and demonstrated improvement. Neither source promises that novelty alone wins.

## Three options

| Direction | User job and visible result | Main unknown | Current judgment |
| --- | --- | --- | --- |
| Contract Medic | A commerce/data team repairs a supplier import and proves its records and amounts. | Real repair reliability and an honest before/after comparison. | Best controlled technical fallback; close event neighbours. |
| Recall Relay (working name) | A small retailer turns an official recall into an accounted-for stock hold and affected-order case. | Resolving missing identifiers and integrating actions without false completion. | Strongest new direction to investigate; different task from the observed repair projects. |
| Access Exit (working name) | An IT operator removes a departing contractor's access and proves no configured access path remains. | Identity/admin access and avoiding service disruption. | Clear result, but substantial existing product overlap and integration risk. |

These judgments concern this hackathon scope, not market size or winning probability. None has customer demand validation. The working names are not checked for availability.

## Proposed Recall Relay task

One sentence: **An agent turns an official product recall into a verified response for one retailer: identify affected stock and orders, hold the affected stock, and prepare the customer action packet.**

A recall notice is the trigger. The agent reads the original notice, inspects catalog and lot records, resolves ambiguous matches using additional evidence, requests clarification when necessary, applies authorised holds in a controlled inventory system, reconciles actual state after failures, and prepares notices for human approval. It stops when each candidate item has a justified outcome or an explicit unresolved question.

It must not infer that an item is unaffected merely because no identifier matched. No real customer messages, refunds, or live stock changes are included in the proposed first version. Proposed actions would execute against a functioning local backend with clearly labelled synthetic inventory and orders. Official recall text would be real; affected-customer counts would be synthetic test outcomes.

## Grounding and counter-evidence

- [CPSC's official API documentation](https://www.cpsc.gov/Recalls/CPSC-Recalls-Application-Program-Interface-API-Information?language=en) describes public recall data in JSON/XML.
- A live, unauthenticated GET of the documented [Toddler query](https://www.saferproducts.gov/RestWebServices/Recall?ProductName=Toddler&format=json) succeeded during this review and returned 78 records. Two inspected examples had September 17 and July 30, 2026 dates. This verifies one public retrieval, not comprehensive coverage, uptime, or a working agent.
- The API examples had empty model/description fields in the structured product entries. The underlying official notice may contain additional detail. This is a real matching limitation and a reason for evidence retrieval or escalation, rather than invented certainty.
- [CPSC's 2010 announcement](https://www.cpsc.gov/Newsroom/News-Releases/2010/CPSC-Makes-Recall-Data-Available-Electronically-to-Businesses-3rd-Party-Developers) explicitly discusses retailers using recall data to flag and stop sales. This is an older documented use case, not evidence of unmet demand today.
- [WatchRecall](https://watchrecall.com/inventory) already advertises inventory upload, exact UPC/model matching, evidence, and rescanning. A generic recall scanner would directly overlap.
- [SafeCart](https://safecart.eu/use-cases/ai-mcp) advertises official EU recall matching, agent access, and webhooks for operational workflows. Do not claim recall agents or recall-triggered actions are globally new.
- [NextStock](https://nextstock.io/features/holds-and-recalls) describes inventory holds and recall ledger operations. A stock hold by itself is not our distinction.
- [Shielded, YC Summer 2026](https://www.ycombinator.com/companies/shielded) illustrates company-specific responses to external supply-chain events. Borrow the link from an outside event to an operational decision; its vendor claims were not reproduced.

The contribution to test is a small agent that finishes an evidenced case despite missing identifiers, changed notices, and ambiguous action failures. This is an implementation hypothesis, not an established market gap or compliance certification.

## Fifteen feature candidates from three perspectives

### Product perspective

1. Carry one notice through to an accounted-for response, rather than only emitting an alert.
2. Include bundles and renamed catalog items in the affected-product investigation.
3. Separate affected, potentially affected, and excluded items with reasons.
4. Keep uncertain cases open with a specific request for missing evidence.
5. Account for stock on hand and previously shipped orders in the same case.

### User experience perspective

1. Show the official notice and the relevant catalog evidence beside each decision.
2. Preview the exact affected items and proposed changes before approval.
3. Explain which identifier or lot range made an item relevant.
4. Make the next human action specific: supply a lot number, approve a notice, or resolve a conflicting identifier.
5. End with a concise case receipt containing action results and remaining questions.

### Engineering perspective

1. Retrieve official recall evidence with source links and observed timestamps.
2. Use deterministic identifier/range checks alongside the model's investigative decisions.
3. Reconcile inventory state after a timeout instead of blindly repeating a hold.
4. Persist the case and resume after worker interruption.
5. Keep the outcome checker outside the agent's editable tools and score fresh cases.

## Five priorities and assumptions to test

| Priority | Why it matters | Assumption / first test |
| --- | --- | --- |
| Evidence-based affected-item resolution | Most of the useful reasoning happens here. | One official notice contains enough criteria to distinguish several synthetic variants; confirm by reading the original notice before building. |
| Explicit uncertain-case handoff | Prevents confident guesses when identifiers are absent. | A model can identify the missing evidence and ask a useful question; compare an ambiguous case with a known match. |
| Executable stock hold with state reconciliation | Makes this a completed task with visible action and recovery. | A small local inventory API is sufficient; simulate a hold that commits before its response is lost. |
| Independent case closure checks | Makes a completion claim falsifiable. | Held-out item/lot labels and actual backend state catch a missed item, a wrong hold, and a duplicate action. |
| Source-linked final receipt and measured traces | Makes the result and improvement understandable in a short demo. | The receipt can show precisely what completed and what remains unresolved, with genuine Neatlogs runs. |

## Smallest complete demo and stopping rule

Use one official consumer-product notice, a small synthetic catalog with clear and ambiguous variants, one inventory/ordering backend, and one agent. Show an alias or lot-range error in the baseline, a failed hold response, the agent's recovery, and independent verification. Any counts must come from the actual run. Do not script a failure or claim an improvement that did not occur.

Neatlogs records the investigation, matching error, action failure, and rerun. Entire records our coding-agent development changes; runtime checkpoint capture is still unverified. cfo.ai models per-retailer pricing, model/job costs, support effort and runway using labelled assumptions and measured usage. AWS is optional hosting. Crustdata should only be added if manufacturer identity data becomes genuinely useful; it is not a dependency of the initial demo.

Before choosing this direction: inspect one complete official notice and manually derive affected/excluded/uncertain examples. If we cannot define the correct actions independently, or the agent adds nothing beyond an exact identifier join, reject or narrow the direction. No runtime, reliability, customer-value or completion claims are currently measured.

Access Exit remains a reserve: [Lumos](https://www.lumos.com/products/lifecycle-management) and [Torii](https://support.toriihq.com/hc/en-us/articles/30079898075291-Offboarding-Employees) already automate offboarding. Torii's documentation also distinguishes workflow completion from actual terminated access in some configurations. A residual-access check is an interesting task, but we have not established access to an identity provider or safe test tenant.

## Decision boundary

This memo expands the options at the user's request. It does not replace the selected Contract Medic direction until the user chooses, and does not authorise outreach, customer messaging, live stock/identity mutations, or additional paid services. The DeepSeek access probe succeeded; no repair or recall agent has been built.
