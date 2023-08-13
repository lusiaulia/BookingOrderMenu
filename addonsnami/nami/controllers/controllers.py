# -*- coding: utf-8 -*-
from odoo import http

# class Nami(http.Controller):
#     @http.route('/nami/nami/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nami/nami/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('nami.listing', {
#             'root': '/nami/nami',
#             'objects': http.request.env['nami.nami'].search([]),
#         })

#     @http.route('/nami/nami/objects/<model("nami.nami"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nami.object', {
#             'object': obj
#         })