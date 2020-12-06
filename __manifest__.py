# -*- coding: utf-8 -*-
{
    'name': "contabilidad",

    'summary': """
       ejemplo de desarrollo en odoo""",

    'description': """
       sistema que permite administrar la contabilidad de la compañia, o yea
    """,

    'author': "Ulises Moreno",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Insurance',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/view_poliza.xml',
        #'views/templates.xml',
    ],
    
}