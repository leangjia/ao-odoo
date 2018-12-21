# Copyright 2018 Eficent Business and IT Consulting Services S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, tools


class MailMessageSubtype(models.Model):
    @tools.ormcache('self.env.uid', 'model_name')
    def _default_subtypes(self, model_name):
        domain = [('default', '=', True),
                  '|', ('res_model', '=', model_name),
                  ('res_model', '=', False),
                  '|', ('id', 'in', self.env.uid.types_to_subscribe)]
        subtypes = self.search(domain)
        internal = subtypes.filtered('internal')
        return subtypes.ids, internal.ids, (subtypes - internal).ids
