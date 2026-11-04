import { Component } from "@odoo/owl";
import { browser } from "@web/core/browser/browser";
import { cookie } from "@web/core/browser/cookie";
import { _t } from "@web/core/l10n/translation";
import { registry } from "@web/core/registry";

export class ColorSchemeToggle extends Component {
    static template = "web_theme_obsidian.ColorSchemeToggle";
    static props = {};

    setup() {
        this.isDark = cookie.get("color_scheme") === "dark";
    }

    get label() {
        return this.isDark ? _t("Switch to light mode") : _t("Switch to dark mode");
    }

    toggle() {
        cookie.set("color_scheme", this.isDark ? "light" : "dark");
        // Fade to the canvas colour first so the reload doesn't flash.
        document.body.classList.add("o_ob_scheme_switching");
        browser.setTimeout(() => browser.location.reload(), 200);
    }
}

registry
    .category("systray")
    .add("web_theme_obsidian.color_scheme", { Component: ColorSchemeToggle }, { sequence: 2 });
