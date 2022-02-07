#-*- coding: utf-8 -*-

from odoo import models, fields, api

class Components(models.Model):
    _name = "cars.components"
    _description = 'cars components'
    _rec_name = 'name'

    name = fields.Char('component name')
