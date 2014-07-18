# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 Andre@ (<a.gallina@apuliasoftware.it>)
#    All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
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
    'name': "Extend l10n_it_ricevute_bancarie",
    'version': '0.1',
    'category': 'account',
    'description': """Estende il modulo ricevute bancarie modificando il campo
data_scadenza in function per legarlo permanentemente
alla scadenze impostate/modificate sulla fattura""",
    'author': 'Andre@ <a.gallina@apuliasoftware.it>',
    'website': 'www.apuliasoftware.it',
    'license': 'AGPL-3',
    "depends": ['l10n_it_ricevute_bancarie'],
    "init_xml": [],
    "update_xml": [],
    "demo_xml": [],
    "active": False,
    "installable": True
}
