# Setup record

Checked on October 10, 2026, IST. Team: **rajkumar guthla**. Team-leader account: **raj315920@gmail.com**.

## Verified

| Service | Result |
| --- | --- |
| Web check-in | Confirmed by the 11:30 AM IST team setup email. |
| Neatlogs | Workspace created; default project `Raj's project`, ID `369facbe-edc4-4e8d-8b81-3bbc39096ff4`. Project SDK key saved in `.env`. |
| Neatlogs entitlement | Billing API reports an active `Legacy unmetered` plan, with no numeric events/projects/teams limits. The project metadata itself reports tier `free`. |
| Neatlogs SDK | Doctor v2 local mode passed on Python SDK 1.4.26. Hosted probe passed visibility, finalization, hierarchy, attributes, input/output, metadata, and typed-token checks. |
| Neatlogs trace readback | CLI authenticated with read scopes, tokens in macOS Keychain, profile `neathack`. Exact probe trace `9bbef0bc2af42458e7e48d10603e2885` finalized successfully, with 4 spans. |
| Crustdata | Email signup completed with promo `NEATLOGS-OCT2026`; API key stored in `.env`. Account API reports **5,200 credits**: 5,000 event credits plus 200 trial credits expiring October 24. Balance UI shows $1,560. |
| Entire | CLI 0.11.4 installed and signed in using the registered Google identity; token in macOS Keychain. Enabled for Codex in this repository. |
| GitHub | Private setup repository: https://github.com/raj921/neatloghackathon. |
| Discord | Signed in as Rajkumar; official neatlogs server and sponsor channels accessible. |
| AWS | Team's shared **$25 allowance** claimed through the private allocation page. Console sign-in succeeded; CLI/SDK profile `neathack` passed STS verification against the assigned IAM user and account. Region `us-east-1`. Existing hackathon VPC and six subnets verified. |

## Credentials and local files

- `.env`: actual Neatlogs project SDK key and Crustdata API key, with file permissions `600`.
- `.secrets/crustdata-account.json`: email and generated Crustdata password, ignored by Git, permissions `600`.
- Neatlogs OAuth and Entire CLI tokens: macOS Keychain.
- AWS event keys: `~/.aws/credentials`, separate `neathack` profile; region in `~/.aws/config`. Files have permissions `600`. Existing default profile retained.
- `.secrets/aws-access.json`: event console login and CLI credentials, ignored by Git, permissions `600`. Private invitation is also stored locally with permissions `600`; it expires 24 hours after delivery.
- `tooling/`: dependency manifest and lockfile for local setup tools.
- `.codex/hooks.json`: Entire hooks and Neatlogs coding-session hooks. Neatlogs hooks load this project's `.env` through `scripts/neatlogs-codex`; no project secret is embedded in the hook definitions.

## Remaining activation steps

### Codex hook trust and first checkpoint

The hook definitions are installed and Neatlogs Codex configuration doctor passes. Entire reports that its seven Codex hooks need approval. Restart/reload Codex, open `/hooks`, and review/trust both Entire and Neatlogs definitions before starting the next coding session. Tool installation does not prove that this current session was captured.

After a fresh captured coding session and a commit, verify a genuine checkpoint:

```sh
entire checkpoint list
entire checkpoint explain HEAD
```

No first captured checkpoint is claimed yet. Automatic transcript pushing is disabled during credential setup. Keep raw setup/authentication transcripts private. Graph, Brain, and Trails are optional and have not been activated for this empty application workspace.

### Entire repository connection

Entire CLI login works through Google. The GitHub identity authorization page kept its Authorize button disabled after a reload, so the GitHub identity/app connection is not confirmed. A troubleshooting request was posted in `#neathack-entire`; response pending. Connect GitHub and grant the Entire app access to only `raj921/neatloghackathon` before using the hosted checkpoint viewer or mirror. Preserve an accessible checkpoint link and ID for the final submission.

## cfo.ai: completion reported by the user

Raj confirmed on October 10 that he completed cfo.ai setup directly. Record this as user-confirmed completion; it supersedes the earlier pending payment-verification status. The agent did not submit payment information.

Subscription status, event-credit balance, and trial cancellation have not been independently verified. The browser session is now under user control, so automated checks remain paused. The team email instructs immediate cancellation in **Settings → Billing** after signup and says event credits will be supplied directly.

## AWS event access: claimed

The organiser's **12:23 PM IST** email, “Your team's $25 AWS access — neatHack”, supplies a private allocation link. Credentials were revealed and securely saved; AWS console sign-in succeeded. Read-only SDK checks confirm the assigned IAM identity, EC2 access, and the existing hackathon network. No infrastructure was provisioned. The allowance comes through this event AWS login; no credit code, new account, or card is required. It is separate from the user's personal AWS account.

- Shared allowance: **$25 for the whole team**, not per member. The access page does not meter spending; $25 is the organiser's allocation, not an independently measured remaining balance.
- Region: **us-east-1 only**. `.env` selects `AWS_PROFILE=neathack` and `AWS_REGION=us-east-1`; `scripts/tool.py aws` explicitly selects both.
- Approved services: **EC2, Lambda, IAM roles, and load balancers only**. Roles and attached policies are permitted. Bedrock is excluded.
- VPC: use the pre-provisioned **`Hackathon_VPC-vpc-vpc`**, ID `vpc-0ae3d3f0fe495c0f8`, for EC2 and load balancers. This is the actual Name tag for the email's `Hackathon_VPC`. Six existing subnets were found. Do not create a new VPC.
- EC2: **one instance per supplied IAM user, shared by the team**. Terminate an existing instance before launching its replacement; automation terminates additional instances. Allowed families are `t2`, `t3`, and `t3a`, sizes `nano`, `micro`, `small`, `medium`, and `large` only.
- EBS: each volume must be **50 GB or less**. Stop resources when finished and stay within the allowance.

Non-secret verification evidence: `docs/aws-access-check.json`. The original Discord request no longer blocks AWS setup. Private login links and credentials must never be shared in Discord, Git, screenshots, or public chats.

### Model provider

No model provider was selected or new inference key created. The event AWS access does not supply Bedrock. Choose a provider when selecting the agent stack; its model API credentials and usage are separate from neatlogs/Crustdata. No model call or idea code was run during setup.

## Official sources reviewed

Recent event emails in the registered Gmail account were reviewed, including the team setup, latest AWS extension, kickoff update, reminders, schedule changes, boarding pass, invitation, and registration confirmation. Newer official guidance takes precedence over older invitation times.

- [Event and requirements](https://neatlogs.com/hackathon/): neatlogs, Entire, and cfo.ai are required. Current event page states building starts October 10 at 12:30 PM IST; submission window October 12, 7:00–11:55 PM IST. Older emails contained different start times.
- [Neatlogs setup guide](https://neatlogs.com/hackathon/neatlogs-setup-guide.html)
- [Neatlogs SDK Doctor](https://docs.neatlogs.com/sdk/doctor)
- [Neatlogs CLI](https://docs.neatlogs.com/cli)
- [Neatlogs Codex hooks](https://docs.neatlogs.com/integrations/codex)
- [Entire neatHack guide](https://hack.entire.io/neathacks-2026/)
- [cfo.ai signup](https://cfo.ai/neathacks)
- [Crustdata CLI](https://docs.crustdata.com/for-agents/cli)
- [AWS sponsor channel](https://discord.com/channels/1528866100207419472/1558110929038614658)
- [cfo.ai sponsor channel](https://discord.com/channels/1528866100207419472/1558110926064975966)

All trace evidence so far is a **synthetic setup probe**, not a real application workflow. No demo, product, business plan, or submission has been created.
