# -*- coding: utf-8 -*-
{
    'name': 'Custom Sales',
    'version': '15.0.1.2.0',
    'summary': 'Custom Sales module built on top of the standard Odoo Sale module.',
    'category': 'Sales/Sales',
    'sequence': 15,
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',

        'views/sale_order_views.xml',
        'views/sale_menus.xml',
    ],

    'installable': True,
    'application': False,
    'auto_install': False,
}
