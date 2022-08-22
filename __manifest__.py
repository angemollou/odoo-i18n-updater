# -*- coding: utf-8 -*-
{
    'name': "odoo_testing",

    'summary': """Overide some translations of the `stock` module""",

    'description': """
        Overide some translations of the `stock` module
    """,

    'author': "angemollou@outlook.com",
    'website': "https://www.upwork.com/freelancers/~0155562fb4d538d083",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Localization',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock'],

    # always loaded
    'data': [
        'data/data.xml',
        # Uncomment following line allows to create ir.translation records directly from a CSV
        # if there are not duplicates
        # 'data/ir.translation.csv',
    ],
}
