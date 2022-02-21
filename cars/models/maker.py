#-*- coding: utf-8 -*-

from odoo import models, fields, api


class Makers(models.Model):
    _name = 'cars.makers'
    _description = 'car maker'
    _rec_name = 'maker'

    maker = fields.Char("maker")
    code = fields.Char("code")
