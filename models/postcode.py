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
    
    
    def _get_postcode(self):
        for rec in self:
            if not rec.part_1:
                rec.part_1 = " "
            if not rec.part_2:
                rec.part_2 = " "
            total = str(rec.part_1) + " " + str(rec.part_2)
            rec.postcode = total
    
    part_1 = fields.Char(string='Part 1')
    part_2 = fields.Char(string='Part 2')
    postcode = fields.Char(compute='_get_postcode', string="Postcode")
    
cm_postcode()
