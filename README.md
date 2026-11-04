# Obsidian — Odoo 19 Backend Theme

A modern skin for the Odoo 19 backend: ink navbar, a single electric-violet accent, editorial typography (Bricolage Grotesque + Plus Jakarta Sans), floating form sheets, lifting kanban cards, and a dark login screen.

- Built on Odoo 19's own SCSS variables (navbar, buttons, fonts, statusbar) — minimal overrides
- Dark colour scheme support (`web.assets_web_dark`)
- Arabic / RTL friendly (IBM Plex Sans Arabic, no letter-spacing on cursive scripts)
- Visible keyboard focus, respects `prefers-reduced-motion`

## Install

1. Clone this repo and add its folder to your `addons_path`.
2. Restart Odoo, update the Apps list.
3. Install **Obsidian Backend Theme** (`web_theme_obsidian`).

Fonts load from Google Fonts; offline servers fall back to system fonts.

## Customize

Brand colour, navbar and fonts: `web_theme_obsidian/static/src/scss/primary_variables.scss`.
Shapes, spacing and motion tokens: top of `backend.scss` (`--ob-*` variables).

License: LGPL-3
