# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.fields import Char, Integer, Many2one


class Components(models.Model):
    _name = "cars.components"
    _description = 'cars components'
    # by default odoo will use the name field as rec_name, if present
    # _rec_name = 'name'
    name = Char('component name')

    quantity = Integer('quantity')
