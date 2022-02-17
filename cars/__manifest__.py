# -*- coding: utf-8 -*-
{
    'name': "cars",

    'summary': """
        Our practical examples""",

    'description': """
        Our practical examples
    """,

    'author': "Luca Alberigo",
    'website': "https://github.com/lucaAlberigo",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/basic.xml',
        'views/inherit.xml',
        'views/components.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
