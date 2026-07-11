# -*- coding: utf-8 -*-
{
    'name': 'Master Data',
    'version': '15.0.1.0.1',
    'summary': 'Master Data Management',
    'description': 'Standalone Master Data module for managing core configuration data.',
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'license': 'LGPL-3',
    'category': 'Master Data',
    'sequence': 10,
    'depends': ['base'],
    'data': [
        # Security must be first
        'security/ir.model.access.csv',

        # Views (each file owns its views, action, and leaf menu item)
        # sales_order_type_views.xml also defines the shared root and
        # Configuration parent menus, so it must be loaded first.
        'views/sales_order_type_views.xml',
        'views/business_type_views.xml',
        'views/business_unit_views.xml',
        'views/unit_part_views.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
