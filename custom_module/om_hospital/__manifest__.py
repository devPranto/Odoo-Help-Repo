# -*- coding: utf-8 -*-
{
    'name': "om_hospital",


    'summary': """
        Hospital Management App """,

    'description': """
        The main purpose is to build and CRM for hospital
    """,
    'application':True,
    'sequence':-100,

    'author': "Pranto Dev",
    'website': "https://www.youtube.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Management',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',

    ],
}
