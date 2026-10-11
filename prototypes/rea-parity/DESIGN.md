# Parity Medic: an inspectable comparison

Read the root DESIGN.md first. This viewer uses its cream background, white surfaces, green accent, thin rules and 8px spacing system. References: design-references/README.md.

The user's journey is outcome → concrete mismatch → repaired result → evidence and limits. It is a read-only view of actual recorded DeepSeek and Neatlogs results. It must never imply that opening the page runs an agent.

- Layout: max width 1120px, 24px outer gutters; title and provenance at top; large comparison separated by a narrow arrow; evidence sections below. A 320px case list sits next to the original/candidate outputs on desktop. Below 800px every comparison stacks and the case list wraps.
- Typography: existing system sans-serif at 16px/1.5. Exception: Georgia title, 48px desktop/36px mobile, regular weight, supporting the document-like evidence view. Monospace only for code and identifiers; tabular numerals for all metrics.
- Color: inherited #f5f5ef background, #202922 text, #59655d muted, #d8ded5 borders, #235b43 accent. Mismatch label #8b302c on #fff1ed; match label uses dark green on #eef5ed. Always pair color with text.
- Spacing and shapes: 8px base; 16px control gaps, 24px panels, 40px sections; 8px panel and 4px control radius. No gradients, shadows, textures or images.
- Components: recorded-run badge; first/final counts; one expandable counterexample at a time; training revision history; full evidence link; scope warning.
- States: native buttons with aria-pressed, min 44px targets and visible 3px focus ring. Errors show an explicit message instead of placeholder scores. Text/code always uses textContent, never untrusted innerHTML.
- Motion: none; recorded numbers must not look like invented live progress. Keyboard and touch work equally. Code blocks wrap and have bounded overflow.
- Claims: say “50 fresh inputs across ten categories”; never “100% reliable,” “production-ready,” “universal parity,” or “new bug in Bruno.” The defect is in a model-generated adapter.
