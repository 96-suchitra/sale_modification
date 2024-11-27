# -*- coding: utf-8 -*-

from odoo import models, fields
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    manager_reference = fields.Text()

    def action_confirm(self):
        sale_order_limit = self.env['ir.config_parameter'].sudo().get_param('sale_modification.sale_order_limit') or 0
        if self.amount_total > float(sale_order_limit) and not self.env.user.has_group('sale_modification.group_sale_admin'):
            raise UserError(("Order Amount exceeds the defined Sale Order Limit (%s)") % ("%.2f" % float(sale_order_limit)))
        return super(SaleOrder, self).action_confirm()

