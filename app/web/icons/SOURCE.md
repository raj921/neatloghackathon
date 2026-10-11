# Phosphor icon assets

These 30 **bold** icons come from the official [Phosphor core repository](https://github.com/phosphor-icons/core/tree/2b75f3ad12b420c9504ef05df8d2564a28f8500e). They retain the designers' original path geometry. No icon geometry was generated or redrawn.

- Pinned commit: `2b75f3ad12b420c9504ef05df8d2564a28f8500e`.
- Official asset directory: [assets/bold](https://github.com/phosphor-icons/core/tree/2b75f3ad12b420c9504ef05df8d2564a28f8500e/assets/bold).
- Copyright: **2023 Phosphor Icons**. The upstream [MIT license](https://github.com/phosphor-icons/core/blob/2b75f3ad12b420c9504ef05df8d2564a28f8500e/LICENSE) is retained verbatim in `LICENSE.txt`.
- `originals/` retains each downloaded upstream SVG byte-for-byte.
- `manifest.json` records every pinned source URL, SHA-256 of the original file, and SHA-256 of its ordered path geometry. Each sprite symbol was compared directly with its original: all path strings are identical and in the original order.
- `phosphor.svg` is a 12,340-byte local sprite. Its SHA-256 is `2250b48be43ef1505b9398d42bf086299a2bb61c89200a1110e45fffb5750a91`.

Only the outer SVG wrapper was replaced with a named `<symbol>`. Each symbol uses `viewBox="0 0 256 256"` and `fill="currentColor"`. The resulting sprite contains only `svg`, `symbol`, and `path` elements, with `id`, `viewBox`, `fill`, and `d` attributes. It contains no scripts, handlers, links, external resources, or embedded content. No library or network request is needed beyond fetching this same-origin static file.

## Usage

Use the ID without the upstream `-bold` suffix:

```html
<svg class="icon" viewBox="0 0 256 256" aria-hidden="true" focusable="false">
  <use href="/assets/icons/phosphor.svg#check-circle"></use>
</svg>
```

Set width and height in CSS (normally 18px for compact controls and 20px for navigation). The icon inherits text color. Give icon-only buttons a useful accessible name and a visible tooltip; keep decorative icons hidden from assistive technology. The `circle-notch` geometry is static: any loading animation belongs in app CSS and should respect reduced motion.

Available IDs: `squares-four`, `clock-counter-clockwise`, `file-text`, `sliders-horizontal`, `magnifying-glass`, `plus`, `arrow-right`, `arrow-down`, `arrow-up-right`, `arrow-left`, `check-circle`, `warning-circle`, `x-circle`, `x`, `copy`, `code`, `git-diff`, `play`, `lightning`, `circle-notch`, `caret-right`, `caret-down`, `moon`, `sun`, `database`, `download-simple`, `checks`, `seal-check`, `dots-three`, `shield-check`.
