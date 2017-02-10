# -*- coding: utf-8 -*-
{
    'name': "adw_custom_quotation",

    'summary': """
        Modifica el formato de la cotización para Adweb Solutions.""",

    'description': """
        Modifica el formato de la cotización para Adweb Solutions.
    """,

    'author': "Adweb Solutions",
    'website': "http://www.adwebsolutions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml','views/sale_custom_fields.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}