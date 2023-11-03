# -*- coding: utf-8 -*-
# Developed By Hector M. Chavez Cortez, Angelica Langarica Escobedo, Kevin Basilio Moreno

{
    'name': 'Partner Status',
    'summary': 'Partner Status',
    'description': 'This module allow users set status in sale orders',
    'author': 'Lucion',
    'website': 'https://lucion.mx',
    'category': 'Tools',
    'version': '1.0',
    'depends': ['base','sale','website_self_cfdi_invoice'],
    'data': [
        'views/res_partner_view.xml',
        'views/sale_order_view.xml',
        'views/template_cfdi.xml',
    ],
    'application': True,
    'installable': True,
}