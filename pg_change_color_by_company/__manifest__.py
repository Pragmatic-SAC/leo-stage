# -*- coding: utf-8 -*-
{
    'name': "Color Theme by Company",

    'summary': "This app change color theme and background image using how was configurated in each company that you have",

    'description': "This app change color theme and background image using how was configurated in each company that you have",

    'author': "Pragmatic S.A.C.",
    'website': "https://pragmatic.com.pe/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'base_sparse_field'],
    'uninstall_hook': 'uninstall_hook',
    'post_init_hook': 'post_init_hook',

    # always loaded
    'data': [
        'views/res_company.xml',
        'views/assets.xml',
    ],
    'auto_install': False,
    'installable': True,
}
