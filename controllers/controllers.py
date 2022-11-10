# -*- coding: utf-8 -*-
# from odoo import http


# class SriLankaAdministrativeDivisions(http.Controller):
#     @http.route('/sri_lanka_administrative_divisions/sri_lanka_administrative_divisions', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sri_lanka_administrative_divisions/sri_lanka_administrative_divisions/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sri_lanka_administrative_divisions.listing', {
#             'root': '/sri_lanka_administrative_divisions/sri_lanka_administrative_divisions',
#             'objects': http.request.env['sri_lanka_administrative_divisions.sri_lanka_administrative_divisions'].search([]),
#         })

#     @http.route('/sri_lanka_administrative_divisions/sri_lanka_administrative_divisions/objects/<model("sri_lanka_administrative_divisions.sri_lanka_administrative_divisions"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sri_lanka_administrative_divisions.object', {
#             'object': obj
#         })
