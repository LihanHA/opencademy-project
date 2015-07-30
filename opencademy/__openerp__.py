# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """Manage trainings""",


    'author': "Ferreteria en Mayoreo SA de CV",
    'website': "http://www.ferreteriaenmayoreo.com.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
       # 'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
       # 'demo.xml',
    ],
    'installable': True,
    'auto_install': False,

}


