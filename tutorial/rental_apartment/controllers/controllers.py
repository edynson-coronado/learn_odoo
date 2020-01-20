# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


"""
class RentalApartment(http.Controller):

    @http.route('/rental_apartment/hello_world', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/rental_apartment/<int:apartment_id>', auth='public')
    def get_object(self, apartment_id, **kw):
        print(apartment_id, type(apartment_id))
        obj = request.env['home.apartment'].sudo().browse(apartment_id)
        return obj.name
"""
