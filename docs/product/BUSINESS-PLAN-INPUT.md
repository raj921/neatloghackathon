# Parity Medic · prepared cfo.ai input

This is a complete planning input, not evidence that cfo.ai generated a plan. Account setup was reported complete by the user; the product plan still needs to be generated and inspected there before claiming that sponsor requirement.

## Product and buyer

Parity Medic helps developers building agents and compatibility wrappers avoid silently changing the behavior of an existing tool. A developer supplies an adapter; the agent reads the original shipped implementation, tests revisions and returns a measured result with a proof. The first supported reference is Bruno 4.2.1, covering deterministic interpolation and JSON request preparation. It does not reconstruct arbitrary applications or send production requests.

The initial buyer is a small developer-tool team that maintains wrappers around stable open-source tools. The user-facing outcome is less manual mismatch investigation, a reproducible contract and evidence that a specific revision preserves supported behavior. The current evidence is a single local repair improving 55/80 to 80/80, plus 80 independently chosen replay inputs. Broader customer impact and willingness to pay remain hypotheses.

## Proposed business model

Start with a free local verifier and optional paid repair/history support. Test a $19/month individual offer with a limited repair allowance and a $99/month team offer with shared evidence, CI integration and private reference storage. These prices are proposals for interviews, not released plans. Avoid promising unlimited model usage. A future hosted edition needs tenant isolation, durable job leases, retention controls and auditable provider consent before selling access.

## Unit-economics assumptions for the plan

The successful prototype repair used three model calls and 28,418 tokens. Neatlogs estimated $0.0117204 for that trace; this is not a provider invoice and omits unsuccessful debugging attempts and hosting. Use a conservative assumed $0.05 per repair for planning, and separately stress-test $0.25 and $1.00. At an assumed 100 repairs/month, inference alone would be $5, $25 or $100 per customer. The proposed individual plan must cap usage or pass through overages under the expensive scenario. Add storage, compute, support and acquisition costs; do not treat inference-only margin as gross margin.

Use three illustrative customer counts (0, 100 and 500), with no claim that any paying customers exist. Distinguish individual/team mix, churn and acquisition spend. Compare a fully local paid-tool distribution with a hosted team service, including operational costs that do not exist in this hackathon prototype.

## Validation and next milestones

1. Interview five developers maintaining wrappers; collect an actual historical mismatch and time-to-diagnose.
2. Add a second independently verified reference contract and a second model provider; measure correct refusals as well as repairs.
3. Run a preregistered evaluation of fresh shapes, supported and unsupported inputs, failure rate, model cost and repair time.
4. Offer a limited paid pilot only after data boundaries and recovery meet the pilot's deployment needs.
5. Prioritize CI evidence exports and reference-version drift before a broad marketplace of reconstructed apps.

## Risks to model explicitly

Finite tests can be overfit; an accepted repair is not universal parity. Original source access and licensing differ by reference tool. Provider behavior/cost can change, and reasoning mode exhausted the prototype budget until configured correctly. Secret-bearing payloads need strict retention and consent. A popular coding agent could incorporate similar functionality, so the product must win on maintained reference contracts and credible verification evidence. Customer demand and measurable time savings are not yet validated.

Ask cfo.ai to produce a business plan using these facts and labelled assumptions, including pricing sensitivity, per-customer cost scenarios, milestones and a validation budget. Preserve the generated plan and its actual provenance for the hackathon demo.
