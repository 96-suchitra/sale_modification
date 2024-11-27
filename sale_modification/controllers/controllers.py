# -*- coding: utf-8 -*-
# from odoo import http


# class SaleModification(http.Controller):
#     @http.route('/sale_modification/sale_modification', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_modification/sale_modification/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_modification.listing', {
#             'root': '/sale_modification/sale_modification',
#             'objects': http.request.env['sale_modification.sale_modification'].search([]),
#         })

#     @http.route('/sale_modification/sale_modification/objects/<model("sale_modification.sale_modification"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_modification.object', {
#             'object': obj
#         })

