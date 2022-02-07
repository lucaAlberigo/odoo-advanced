#-*- coding: utf-8 -*-

from odoo import models, fields, api


class Cars(models.Model):
    _name = 'cars.cars'
    _description = 'cars.cars'
    _rec_name = 'name'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float()
    description = fields.Text()

    valueA = fields.Char('A')
    valueB = fields.Char('B')
    valueC = fields.Char('C')
    valueD = fields.Char('D')

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
