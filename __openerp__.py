# -*- encoding: utf-8 -*-
##############################################################################
#Copyright (c) 2015 - Present Teckzilla Software Solutions Pvt. Ltd. All Rights Reserved
#    Author: [Teckzilla Software Solutions]  <[sales@teckzilla.net]>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    A copy of the GNU General Public License is available at:
#    <http://www.gnu.org/licenses/gpl.html>.
#
##############################################################################


{
    'name': 'CM Branch',
    'version': '1.0',
    'category': 'Generic Modules/Warehouse Management',
    'description': """
     CM Branch
    """,
    "website" : "www.teckzilla.net",
    'author': 'Teckzilla Software Solutions',
    'depends': ['cm'],
    "demo" : [],
    "data": [
        'view/branch_view.xml',
        'view/postcode_view.xml',
        'view/wcfmc_account_view.xml',
        'view/wcfmc_account_import_view.xml',
    ],
    'auto_install': False,
    'installable': True,
}
