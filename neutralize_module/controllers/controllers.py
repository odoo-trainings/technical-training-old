# -*- coding: utf-8 -*-
# from odoo import http


# class NeutralizeModule(http.Controller):
#     @http.route('/neutralize_module/neutralize_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/neutralize_module/neutralize_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('neutralize_module.listing', {
#             'root': '/neutralize_module/neutralize_module',
#             'objects': http.request.env['neutralize_module.neutralize_module'].search([]),
#         })

#     @http.route('/neutralize_module/neutralize_module/objects/<model("neutralize_module.neutralize_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('neutralize_module.object', {
#             'object': obj
#         })
