# -*- coding: utf-8 -*-
{
    'name': "Sri Lanka Administrative Divisions",

    'summary': """
        Provinces, Districts, Cities of Sri Lanka""",

    'description': """
        Provinces, Districts, Cities of Sri Lanka
    """,

    'author': "Tharindu Mayuranga",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','web_domain_field',],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/provinces.xml',
        'views/districts.xml',
        'views/cities.xml',
        # 'views/menu.xml',
        'data/ad.provinces.csv',
        'data/ad.districts.csv',
        'data/ad.cities.csv',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
