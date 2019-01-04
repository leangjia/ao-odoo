# Copyright 2017 Eficent Business and IT Consulting Services S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models, _


class CrmHelpdesk(models.Model):
    """ Helpdesk Cases """

    _inherit = "crm.helpdesk"

    def _get_default_priority(self):
        if self.partner_id:
            return self.partner_id.helpdesk_default_priority

    priority = fields.Selection(
        default=_get_default_priority
    )

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id and self.partner_id.helpdesk_default_priority:
            self.priority = self.partner_id.helpdesk_default_priority
