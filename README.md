# Obsidian — Odoo 19 Backend Theme

A modern skin for the Odoo 19 backend: night-indigo aurora navbar, an indigo→violet gradient accent, Tajawal typography (Arabic + Latin), roomy spacing, floating form sheets and list cards, lifting kanban cards, and a glowing dark login screen.

- Built on Odoo 19's own SCSS variables (navbar, buttons, fonts, statusbar) — minimal overrides
- **Dark mode toggle** in the navbar (sun/moon). Ships its own dark palette, so it works on Community; remembered per browser
- **Modern loaders**: Odoo's corner "Loading" box becomes a glowing top progress bar; the full-screen wait gets frosted glass, a gradient ring and calm messages (Arabic included)
- Arabic / RTL friendly: Tajawal for both scripts, no letter-spacing on cursive text
- Visible keyboard focus, respects `prefers-reduced-motion`

## Install

1. Clone this repo and add its folder to your `addons_path`.
2. Restart Odoo, update the Apps list.
3. Install **Obsidian Backend Theme** (`web_theme_obsidian`).

Fonts load from Google Fonts; offline servers fall back to system fonts.

## Customize

Brand colour, navbar and fonts: `web_theme_obsidian/static/src/scss/primary_variables.scss`.
Spacing, radii and font size: same file (`$o-horizontal-padding`, `$o-border-radius*`, `$o-font-size-base`).
Colours, shadows and motion tokens: top of `backend.scss` (`--ob-*` variables); dark palette in `backend.dark.scss`.

License: LGPL-3
