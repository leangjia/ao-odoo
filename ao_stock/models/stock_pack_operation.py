# -*- coding: utf-8 -*-
# Copyright 2017 Eficent Business and IT Consulting Services S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class StockPicking(models.Model):
    _inherit = "stock.pack.operation"

    @api.one
    def _compute_qty_available_in_source_loc(self):
        product_available = self.product_id.with_context(
            location=self.location_id.id)._product_available()[
            self.product_id.id]
        self.qty_available_in_source_loc = product_available[
            'qty_available_not_res']

    qty_available_in_source_loc = fields.Float(
        compute=_compute_qty_available_in_source_loc)
