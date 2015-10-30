# -*- encoding: utf-8 -*-
##############################################################################
#    Copyright (c) 2015 - Present Teckzilla Software Solutions Pvt. Ltd. All Rights Reserved
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

from openerp import models, fields, api, _

class cm_postcode(models.Model):
    _name = "cm.postcode"
    
    area = fields.Char(string='Area Code', help="Three character area code, for example BN3 or N1C", required=True)
    branch_ids = fields.Many2many('cm.branch', 'branch_postcode_rel', 'postcode_id', 'branch_id', 'Branches')

    @api.model
    def create(self, vals):
    	vals['area'] = (vals.get('area') or '').upper()
    	return super(cm_postcode, self).create(vals)
    
cm_postcode()
