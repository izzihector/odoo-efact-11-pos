# -*- coding: utf-8 -*-
#################################################################################
# Author      : Acespritech Solutions Pvt. Ltd. (<www.acespritech.com>)
# Copyright(c): 2012-Present Acespritech Solutions Pvt. Ltd.
# All Rights Reserved.
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#################################################################################

{
    'name': 'POS Kitchen Screen',
    'category': 'Point of Sale',
    'summary': "POS Kitchen Screen",
    'description': "POS Kitchen Screen shows orders and their state to Cook and Manager",
	'author': "Acespritech Solutions Pvt. Ltd.",
    'website': 'http://www.acespritech.com',
	'price': 30.0,
    'currency': 'EUR',
    'version': '1.0',
    'depends': ['point_of_sale','bus','pos_restaurant'],
    'images': ['static/description/main_screenshot.png'],
    'data': [
        'views/res_users_view.xml',
        'views/pos_kitchen_screen.xml',
        'views/kitchen_screen_view.xml',
    ],
    'qweb': ['static/src/xml/pos.xml'],
    'installable': True,
    'auto_install': False
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
