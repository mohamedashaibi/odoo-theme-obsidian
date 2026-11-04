{
    "name": "Obsidian Backend Theme",
    "summary": "Ink navbar, violet accent, editorial typography for the Odoo backend",
    "version": "19.0.1.0.0",
    "category": "Themes/Backend",
    "license": "LGPL-3",
    "depends": ["web"],
    "data": ["views/webclient_templates.xml"],
    "assets": {
        # Prepended so our values win over Odoo's `!default` declarations.
        "web._assets_primary_variables": [
            ("prepend", "web_theme_obsidian/static/src/scss/primary_variables.scss"),
        ],
        "web.assets_backend": [
            "web_theme_obsidian/static/src/scss/backend.scss",
        ],
        "web.assets_web_dark": [
            "web_theme_obsidian/static/src/scss/backend.dark.scss",
        ],
        "web.assets_frontend": [
            "web_theme_obsidian/static/src/scss/login.scss",
        ],
    },
    "installable": True,
    "application": False,
}
