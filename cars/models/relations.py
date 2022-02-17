# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Cars(models.Model):
    _inherit = 'cars.cars'

    parts = fields.One2many('cars.car_parts', 'car')


class CarParts(models.Model):
    _name = 'cars.car_parts'
    _description = 'various parts'

    car = fields.Many2one('cars.cars', "car id")
    part = fields.Many2one('cars.components', "part id")
    quantity = fields.Integer('count', default=1)
    # cost = fields.Monetary('Cost')
    color = fields.Char('part color RGB')
