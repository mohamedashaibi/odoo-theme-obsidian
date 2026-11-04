import { Component } from "@odoo/owl";
import { browser } from "@web/core/browser/browser";
import { cookie } from "@web/core/browser/cookie";
import { _t } from "@web/core/l10n/translation";
import { registry } from "@web/core/registry";
import { user } from "@web/core/user";

export class ColorSchemeToggle extends Component {
    static template = "web_theme_obsidian.ColorSchemeToggle";
    static props = {};

    setup() {
        this.isDark = cookie.get("color_scheme") === "dark";
        this.switching = false;
    }

    get label() {
        return this.isDark ? _t("Switch to light mode") : _t("Switch to dark mode");
    }

    async toggle() {
        if (this.switching) {
            return;
        }
        this.switching = true;
        const next = this.isDark ? "light" : "dark";
        // Enterprise's color_scheme service re-derives the scheme from the
        // user's res.users.settings on every load and overwrites the cookie,
        // so the preference must be saved there first. Community has no such
        // field (and no such service), so the cookie alone is enough.
        if ("color_scheme" in user.settings) {
            await user.setUserSettings("color_scheme", next);
        }
        cookie.set("color_scheme", next);
        // Fade to the canvas colour first so the reload doesn't flash.
        document.body.classList.add("o_ob_scheme_switching");
        browser.setTimeout(() => browser.location.reload(), 200);
    }
}

registry
    .category("systray")
    .add("web_theme_obsidian.color_scheme", { Component: ColorSchemeToggle }, { sequence: 2 });
