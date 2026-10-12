# Submission checklist · checked October 12, 2026

## Confirmed requirements

Source: [official event](https://neatlogs.com/hackathon), with [organizer announcements](https://discord.com/channels/1528866100207419472/1555114630966153265) checked this morning.

- Build a substantial end-to-end agent during the event; publish dated code commits.
- Teams have 1–4 registered members, a consistent team name and one team per person.
- Use Neatlogs, Entire and cfo.ai. Preserve before/after numbers, failure recovery, traces, graph/checkpoint evidence and a financial plan covering pricing, costs, revenue and runway.
- Submit one project through a public X quote post attaching the official submission post. Include team, builder name, project, public repository and demo link.
- One video, at most three minutes, must explain the problem and all three required tools, with their implementation and results. Today's organizer announcement additionally asks for critical-incident investigation and resolution in Neatlogs.
- Publish genuine build updates tagged #neatHack. No spam, plagiarism, harassment, purchased likes or bots.
- Submission opens October 12 at 19:00 IST; planned close 23:55 IST. Discord controls the final cutoff. Draft creation alone is not submission.
- AWS, Crustdata and model credits are optional; they do not replace the three mandatory tools.

## Project evidence and remaining work

| Item | Current evidence / action |
| --- | --- |
| Team and check-in | Organizer email supplied by builder confirms `rajkumar guthla`, Raj Kumar, completed check-in. |
| Dated implementation | Product commits on October 11. Earlier October 10 commits are setup and research. |
| Public repository | [raj921/neatloghackathon](https://github.com/raj921/neatloghackathon), public; default branch `codex/parity-medic-product`. Public HTTP 200 confirmed October 12. |
| Publication review | Inspected 176 distinct history blobs for recognized key/private-key formats: no matches. No `.env`, `.secrets`, `.local` or `.entire/logs` paths in Git history. Current authentication-link pattern inspection found no matches. This is a bounded review, not a security certification. |
| Repair evidence | [Actual request repair](../../app/evidence/request-live.json): 55/80 before, 80/80 after, separate 80/80 replay, 3 calls, 28,418 tokens. Finite supported comparisons only. |
| Failure and recovery | [Diagnostic attempt](../../app/evidence/repair-diagnostic.json): reasoning exhausted output budget; no candidate accepted. [Product review](../product/REVIEW.md) records the non-thinking/required-tool correction and successful rerun. |
| Neatlogs | [Remote readback](../../app/evidence/neatlogs-request-readback.json). Actual incident `15b2ca92-b68d-46b9-82bd-0e1bdcecf35b` created from saved failed traces October 12. Incident explanation overstates the retry/cause evidence; correction requests encountered connection failures. A native incident investigation is in progress. |
| Entire | [Product source graph](../../app/evidence/entire-product-search.json). Graph output qualifies; no checkpoint is claimed. |
| cfo.ai | [Ari-generated plan](evidence/business-plan.pdf), [financial model](evidence/financial-model.xlsx) and [provenance](evidence/cfo-provenance.json) downloaded and inspected October 12. Prices, customers and starting cash are hypothetical. [Shared page](https://cfo.ai/s/jmbAAAxR7or4ofo6). |
| Demo | Existing local 171.307-second cut requires incident and cfo.ai footage/narration revisions. Public link pending. |
| Vercel | Account access confirmed. Hosting pending: local SQLite and a background worker cannot safely be treated as durable Vercel Functions. |
| Build in public | [Published #neatHack build update](https://x.com/RajKuma39078041/status/2109504063452905617), read back October 12; not a final quote submission. |
| Final quote post | Not published. Await official submission post and window. Recheck instructions and final cutoff immediately before publication. |

No submission receipt is claimed. Preserve the final public X URL and verify its attached official post and working repository/demo links before marking submitted.
