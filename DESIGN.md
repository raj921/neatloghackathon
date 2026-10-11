# Recall Relay: calm containment workbench

This direction serves one decision: which stock may be sold, which must be held, and what still needs physical evidence. Sources, uncertainty and action history matter more than decorative metrics. References: `design-references/README.md`.

## Shared constraints

- Typography: system sans-serif; 16px body, 14px secondary, 36px title; line-height 1.5. Monospace only for identifiers. Tabular numerals for quantities.
- Colors: background `#f5f5ef`, surface `#ffffff`, text `#202922`, muted `#59655d`, rule `#d8ded5`, one accent `#235b43`. Status labels include words; never rely on color alone.
- Spacing: 8px base; 16px control gaps, 24px panels, 40px section gaps. Max content width 1120px with 24px outer gutters.
- Shape: 8px cards, 4px controls, 1px borders; no shadows, gradients, shaders or decorative images.
- Components: source panel; stock table; order dispositions; action ledger; free-play controls; guided scenario tabs. Mark the walkthrough **simulation** permanently. Real model-run results remain separate JSON evidence.
- States: exact match means **Hold**; excluded means **Clear for this recall**; unknown means **Review, fulfilment blocked**. Case completion means containment with unresolved evidence, not a claim that every item is safe.
- Interaction: native buttons, descriptive labels, visible 3px focus ring, 44px minimum targets. Actions announce their result in a polite live region. No animation or network calls in the HTML walkthrough.
- Responsive: two-column source/state layout above 800px; single column below. Tables scroll inside their panel and controls wrap. No page-wide horizontal scrolling at 375px.

## Prototype exception

The state HTML is a throwaway, self-contained learning artifact on `codex/recall-relay-prototype`, not a shipped application or a real-model dashboard. Its controls intentionally expose illegal transitions so people can test the rules. The backend proof calls DeepSeek and Neatlogs separately; no credentials enter the HTML.
