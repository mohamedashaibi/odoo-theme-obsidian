import { _t } from "@web/core/l10n/translation";
import { BlockUI } from "@web/core/ui/block_ui";
import { patch } from "@web/core/utils/patch";

// Calm, informative copy for the full-screen wait instead of Odoo's jokes.
// `time` = seconds before moving to the next message (null = final).
patch(BlockUI.prototype, {
    setup() {
        super.setup(...arguments);
        this.messagesByDuration = [
            { time: 15, l1: _t("Loading…") },
            { time: 30, l1: _t("Still working on it…") },
            {
                time: 60,
                l1: _t("This is taking longer than usual."),
                l2: _t("Hang tight, it's still running."),
            },
            {
                time: null,
                l1: _t("Still running in the background."),
                l2: _t("If nothing changes, try reloading the page (F5)."),
            },
        ];
    },
});
