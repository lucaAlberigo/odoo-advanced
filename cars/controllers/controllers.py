# -*- coding: utf-8 -*-
# from odoo import http


# class Cars(http.Controller):
#     @http.route('/cars/cars/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cars/cars/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cars.listing', {
#             'root': '/cars/cars',
#             'objects': http.request.env['cars.cars'].search([]),
#         })

#     @http.route('/cars/cars/objects/<model("cars.cars"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cars.object', {
#             'object': obj
#         })
