# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Cars(models.Model):
    _inherit = 'cars.cars'

    optional_package = fields.Many2one('cars.optionals', 'Optional Package')
    filter = fields.Char(related="optional_package.filter_code", string='package filter')
    paint = fields.Many2one('cars.paints')

    @api.onchange('optional_package')
    def clear_paint(self):
        self.paint = 0


class Paints(models.Model):
    _name = 'cars.paints'
    _description = 'paint colors for cars'
    _rec_name = 'color'

    color = fields.Char('color')
    code = fields.Char('code')
    price = fields.Integer('price')
    filter = fields.Char('filter')


class Optionals(models.Model):
    _name = 'cars.optionals'
    _description = 'optionals packages'

    name = fields.Char('optional package')
    filter_code = fields.Char('code')
    price = fields.Float('price')
