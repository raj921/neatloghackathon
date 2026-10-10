# Scope

This repository currently contains hackathon setup only. Do not build idea code or choose an application framework until the user asks. Read `docs/SETUP.md` for the account status and evidence boundaries. Never commit `.env`, `.secrets`, authentication links, or raw credential-setup transcripts.

# Frontend design references

For every frontend creation, redesign, or UI editing task, consult this reference list before choosing typography, textures, themes, spacing, motion, or number displays. Open the relevant sites for current examples and documentation before applying their resources.

- [Uncut](https://uncut.wtf): curated free typefaces for distinctive typography.
- [Paper Shaders](https://shaders.paper.design): lightweight shaders for backgrounds and textures.
- [tweakcn](https://tweakcn.com): visual theme editor for customizing shadcn/ui beyond its default appearance.
- [DialKit](https://dialkit.dev): live controls for tuning spacing, motion, and colors in the running app.
- [Number Flow](https://number-flow.barvian.me): animated numbers for intentional, polished value changes.

Use these references to make deliberate design choices suited to the product and its existing stack. Choose applicable resources; add libraries or effects only when they improve the requested frontend. Keep typography readable, motion accessible, and performance appropriate to the target devices.

## Visual direction and design system

Before building any screen, choose a visual direction aligned with the product's mechanics, user journeys, and intended outcomes. Consult relevant inspiration from:

- [Design for B2B](https://designforb2b.com)
- [Minimal Gallery](https://minimal.gallery)
- [Search System](https://searchsystem.co)
- [Dark Design](https://dark.design)
- [Ogo Inspo](https://ogoinspo.com)
- [A1 Gallery](https://a1.gallery)
- [Umanmade](https://umanmade.com)
- [Logggos](https://logggos.club)
- [MNMM](https://mnmm.xyz)

For a new frontend or client build, first prepare a project folder of 5–6 visual references and a `DESIGN.md` file. Record reference links or supplied images with short notes explaining which visual decisions they inform. Turn the chosen direction into concrete constraints for typography, colors, spacing, radius, shadows, components, interaction states, and responsive behavior. Explain how those choices support the product's mechanics and outcome goals.

Read `DESIGN.md` before implementing each screen and follow its shared constraints across screens. For an existing project, reuse and update its design document and reference folder so edits remain consistent. Keep intentional exceptions documented.

When working in Claude Code or Cursor, include `DESIGN.md` in the agent's project context. If a `/design` command is available, use it to describe what should remain consistent across every screen. Make the written constraints specific enough for implementation and review.
