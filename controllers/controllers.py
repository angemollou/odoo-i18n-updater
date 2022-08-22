# -*- coding: utf-8 -*-
# from odoo import http


# class OdooTesting(http.Controller):
#     @http.route('/odoo_testing/odoo_testing/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_testing/odoo_testing/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_testing.listing', {
#             'root': '/odoo_testing/odoo_testing',
#             'objects': http.request.env['odoo_testing.odoo_testing'].search([]),
#         })

#     @http.route('/odoo_testing/odoo_testing/objects/<model("odoo_testing.odoo_testing"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_testing.object', {
#             'object': obj
#         })
