from odoo import models
from odoo.http import request


class IrHttp(models.AbstractModel):
    _inherit = "ir.http"

    def color_scheme(self):
        # The navbar toggle stores the choice per browser in the `color_scheme`
        # cookie (same cookie Enterprise uses). Only the exact value "dark" is
        # honoured; anything else falls through to Odoo's default.
        if request and request.httprequest.cookies.get("color_scheme") == "dark":
            return "dark"
        return super().color_scheme()
