# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Cars(models.Model):
    _inherit = 'cars.cars'

    # one2many needs a corresponding many2one field on the corresponding model that loops back
    parts = fields.One2many('cars.car_parts', 'car')

    #make a filter using a many2one
    # maker = fields.Many2one('Maker')


class CarParts(models.Model):
    _name = 'cars.car_parts'
    _description = 'various parts'

    # corresponding field that loops back,
    # do not show in views, will be autocompleted on save
    car = fields.Many2one('cars.cars', "car id")

    part = fields.Many2one('cars.components', "Part")
    quantity = fields.Integer('count', default=1)
    # cost = fields.Monetary('Cost')
    color = fields.Char('part color RGB')
