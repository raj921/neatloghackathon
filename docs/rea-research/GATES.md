# Gates: REA-informed hackathon direction

OWNS: docs/rea-research/**, prototypes/rea-*

Scope: inspect REA and an obtainable reference application, refresh event competition and product inspiration, choose a differentiated feasible task, and implement its smallest measurable proof if the research supports it.

- [x] G1: REA architecture findings trace to pinned public source and distinguish documented capabilities from locally observed behavior.
  EVIDENCE: DECISION.md identifies pinned commit 21650455a9c90a26e725c3505a3c17054cc4516c and actual service, artifact-reader and worker code; evidence/rea-summary.json records six parsed JS files, incomplete slice coverage and a semantic-budget limit; model source selection remains host-selected.

- [x] G2: Current Discord build observations and official requirements are recorded with dates and links, without claiming the sample covers every entrant.
  EVIDENCE: DECISION.md records October 11 FirstRun, benana and GBA posts with exact message links; the FirstRun site and benana X post were inspected in the signed-in browser. Current official rubric and required tools were reread; earlier Medic/Upshift observations are labelled historical, sample coverage is explicit.

- [x] G3: Recent product inspiration and the supplied winning-ideas article are compared against concrete user tasks, existing competitors, sponsor roles, visible demo results and feasibility risks.
  EVIDENCE: DECISION.md compares dated Product Hunt listings, YC companies, Frigade, SkillWeaver, mcp-drift and primary research against a specific adapter-repair job; it rejects universal app-to-agent, generic QA and sandbox-factory claims, and applies the supplied article as heuristics rather than a winning prediction.

- [x] G4: The downloaded app identity, differential oracle positive and negative controls, bounded candidate execution, and static REA evidence pass.
  CWD: ../..
  CHECK: .venv/bin/python prototypes/rea-parity/agent.py --self-check
  EXPECT: PARITY_CONTROLS_VERIFIED
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/Users/rajkumar/neatloghackathon; path=85e77dcef6af/67 entries; EXPECT=matched; output-sha256=21b49159b0a9d54db2ba05f4c3e229825fb94ec535ddfac21787db47d64bc4a3; output-bytes=25

- [x] G5: A real DeepSeek tool loop submits an adapter that agrees with the downloaded app on the declared fresh input set.
  CWD: ../..
  CHECK: .venv/bin/python prototypes/rea-parity/agent.py --live
  EXPECT: APP_ORACLE_AGENT_VERIFIED
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/Users/rajkumar/neatloghackathon; path=85e77dcef6af/67 entries; EXPECT=matched; output-sha256=a6170acbbbd97eead892fc4392cfd599e390eff4feff3ac92eb915c0c1f1a176; output-bytes=3242

- [x] G6: Final claims are reconciled with artifacts, source links, originality limits and actual sponsor/provider round trips.
  EVIDENCE: evidence/review.json reconciles 25/50 to 50/50, five calls and 21275 tokens with the finalized 13-span Neatlogs export; stored counterexample readback confirmed the intermediate 18/20 failure. Browser verified case selection and 390px no-overflow layout; allowlisted server rejected credential paths. Artifact scan found no configured secret values. Bruno attribution and MIT notice are preserved; cfo plan, public sharing, workflow expansion and production readiness remain explicitly unclaimed.
