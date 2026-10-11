# Parity Medic — an evidence workbench

Read before each screen. References: `design-references/parity-medic/README.md`. Prior prototypes remain unchanged. Product: disagreement → original behavior → repair → finite verification → reusable export. Distinguish recorded research, local checks, live model work and human review.

## Direction and typography

Editorial engineering workbench: warm white canvas, forest green actions, quiet rail, expansive comparisons and precise rules. Refero's concrete specs inform hierarchy; cinematic bookmark references inform restraint. No fake illustration, decorative shader, fabricated metrics or simulated reasoning.

Self-hosted Uncut Sans 400–700, font-display swap, body 15px/1.55, helpers 13px. Georgia is a deliberate display exception: main result 42px/1.08 desktop, 32px mobile. Code ui-monospace 12px/1.65; identifiers wrap; tabular numbers. No fake count-up for saved results.

## Tokens

Canvas #f7f8f5, surface #fff, rail #f0f3ed, ink #202b24, secondary #58645c, rule #dce2d8, accent #245a42, accent-soft #e7efe6. Error #9b382d on #faeeeb; review #795116 on #f8f0df. Status includes words.

Dark mode entire app: canvas #151c18, surface #1e2821, rail #19231c, ink #ecf0e9, secondary #acb9ae, rules #354339, accent #afd4ae with dark button text. Code theme tokens.

4px base; 8/12/16/24/32/48 spacing. Max 1360px; rail 232px; gutters 40px desktop/20px mobile. Control radius 8px, panel 12px, 1px border; shadow only dialogs/toasts.

## Screens and states

Functional destinations Workbench, Run history, Evidence, Settings. Main screen source breadcrumb, measured result, scope caption, primary action, input/adapter area, before/reference/after comparison. Tabs history/patch/proof. New verification uses labelled native dialog, contract selection, source, JSON, validation, provider disclosure and cost ceiling. History search/persistent rows/reopen without work. Settings expose readiness, never keys. Export includes hashes, inputs/seeds/counts/source; finite tests never mean universal compatibility.

Buttons/links minimum 44px; visible 3px keyboard focus; native dialog Escape restores focus; polite status region. Real running labels may use Transitions.dev shimmer. 160–220ms opacity/transform, reduced-motion guard; no auto-scroll while reading. Errors preserve inputs/evidence. Cancel and review have distinct state. Downloads only for eligible artifacts.

Under 900px rail becomes compact top navigation; comparisons stack. Code/table scroll internally; no page overflow at 390px; dialog fits 320px.
