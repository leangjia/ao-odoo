# Copyright 2016 Eficent Business and IT Consulting Services S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class StockChangeStandardPrice(models.TransientModel):
    _inherit = "stock.change.standard.price"

    @api.model
    def default_get(self, fields):
        res = super(StockChangeStandardPrice, self).default_get(fields)
        if self.env.context.get('bom_standard_cost', False):
            products = self.env[
                self._context['active_model']].browse(
                self._context['active_ids'])
            for product in products:
                res['new_price'] = product.bom_standard_cost
        return res

    @api.multi
    def change_price(self):
        if self.env.context.get('bom_standard_cost', False):
            if self._context['active_model'] == 'product.template':
                products = self.env['product.template'].browse(
                    self._context['active_ids']).product_variant_ids
            else:
                products = self.env['product.product'].browse(
                    self._context['active_ids'])
            for product in products:
                if (product.valuation != 'real_time' or
                        product.cost_method == 'standard'):
                    product.do_change_standard_price(
                        product.bom_standard_cost,
                        self.counterpart_account_id.id)
            return {'type': 'ir.actions.act_window_close'}
        super(StockChangeStandardPrice, self).change_price()
