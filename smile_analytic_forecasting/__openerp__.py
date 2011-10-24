# -*- coding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011-2012 Smile (<http://www.smile.fr>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     
#
##############################################################################

{
    "name" : "Smile Analytic Forecasting",
    "version": "0.1",
    "author" : "Smile",
    "website" : "http://www.smile.fr",
    "category" : "Generic Modules/Accounting",
    "depends" : ["smile_analytic_period"],
    "description": """Forecasting Analytic Account""",
    "init_xml" : [
        'security/ir.model.access.csv',
    ],
    "update_xml": [
        'analytic_view.xml',
        'report/analytic_report_view.xml',
    ],
    'demo_xml': [],
    'installable': True,
    'active': False,
    'certificate' : "",
}