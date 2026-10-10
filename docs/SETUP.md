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
| AWS tooling | AWS CLI 2.31.39 installed; existing default profile passed STS identity verification. This does **not** establish event-credit eligibility. |

## Credentials and local files

- `.env`: actual Neatlogs project SDK key and Crustdata API key, with file permissions `600`.
- `.secrets/crustdata-account.json`: email and generated Crustdata password, ignored by Git, permissions `600`.
- Neatlogs OAuth and Entire CLI tokens: macOS Keychain.
- Existing AWS credentials: existing AWS configuration; never copied into Git or a new project key file.
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

Entire CLI login works through Google. The GitHub identity authorization page kept its Authorize button disabled after a reload, so the GitHub identity/app connection is not confirmed. Connect GitHub and grant the Entire app access to only `raj921/neatloghackathon` before using the hosted checkpoint viewer or mirror. Preserve an accessible checkpoint link and ID for the final submission.

### cfo.ai

Signed in with the registered Google account. Reached Startup trial signup and the payment verification form. No card was submitted, no subscription activated, and no cancellation is claimed.

Complete payment verification directly in the browser if using the trial. The team email instructs immediate cancellation in **Settings → Billing** after signup; verify cancellation before considering this step complete. The neatHack team says it will supply credits directly. A card-free activation question was posted in `#neathack-cfo-ai` at 11:49 AM IST; response pending.

### AWS event access

The 11:26 AM IST organiser email extended eligibility to the first 400 checked-in teams. No event activation email or credentials were found in the team-leader inbox. A request was posted in `#neathack-aws` at 11:43 AM IST for eligibility confirmation and private delivery of activation details; response pending.

The AWS sponsor channel says the allowance is **$25 per team** for the approved services listed in its activation email, and **Bedrock is excluded**. Do not assume this allowance applies to the user's existing default AWS account. Once the organiser provides details, configure a separate `neathack` profile and set `AWS_PROFILE=neathack` in `.env`. Use the region and authentication method in that email. Do not provision infrastructure until account, allowance, and permitted services are confirmed.

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
