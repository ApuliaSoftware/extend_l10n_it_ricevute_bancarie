# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 Andre@ (<a.gallina@cgsoftware.it>)
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

from osv import osv
from tools.translate import _
import logging

_logger = logging.getLogger('Test RIBA')


class account_invoice(osv.osv):

    _inherit = "account.invoice"

    def action_cancel(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        invoices = self.read(cr, uid, ids, ['move_id', 'payment_ids'])
        move_ids = []
        for i in invoices:
            if i['move_id']:
                move_ids.append(i['move_id'][0])
        if move_ids:
            move_line_ids = self.pool.get('account.move.line').search(
                cr, uid, [('move_id', 'in', move_ids)])
            dist_line_ids = self.pool.get('riba.distinta.move.line').search(
                cr, uid, [('move_line_id', 'in', move_line_ids)])
            stop = False
            if dist_line_ids:
                for line in self.pool.get('riba.distinta.move.line').browse(
                        cr, uid, dist_line_ids, context):
                    if line.riba_line_id:
                        if line.riba_line_id.state == 'draft':
                            # -- code to delete line
                            self.pool.get('riba.distinta.line').unlink(
                                cr, uid, line.riba_line_id.id, context)
                        else:
                            stop = True
            if stop:
                raise osv.except_osv(
                    _('Errore'),
                    _('Non puoi annullare una fattura con delle riba emesse \
                      annulla prima la distinta'))

        return super(account_invoice, self).action_cancel(cr, uid,
                                                          ids, context)
