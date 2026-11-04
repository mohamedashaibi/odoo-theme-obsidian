{
    "name": "Obsidian Backend Theme",
    "summary": "Night-indigo navbar, violet gradient accent, Tajawal typography, dark mode toggle",
    "version": "19.0.1.3.1",
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
            "web_theme_obsidian/static/src/color_scheme/*",
            "web_theme_obsidian/static/src/loading/*",
        ],
        # Dark palette, loaded when the `color_scheme` cookie is "dark".
        "web.assets_web_dark": [
            ("include", "web_theme_obsidian._assets_dark_variables"),
            "web_theme_obsidian/static/src/scss/backend.dark.scss",
        ],
        "web.assets_backend_lazy_dark": [
            ("include", "web_theme_obsidian._assets_dark_variables"),
        ],
        "web_theme_obsidian._assets_dark_variables": [
            ("before", "web/static/src/scss/primary_variables.scss",
             "web_theme_obsidian/static/src/scss/primary_variables.dark.scss"),
            ("before", "web/static/src/scss/bootstrap_overridden.scss",
             "web_theme_obsidian/static/src/scss/bootstrap_overridden.dark.scss"),
            ("after", "web/static/lib/bootstrap/scss/_functions.scss",
             "web_theme_obsidian/static/src/scss/bs_functions_overrides.dark.scss"),
        ],
        "web.assets_frontend": [
            "web_theme_obsidian/static/src/scss/login.scss",
        ],
    },
    "installable": True,
    "application": False,
}
