# -*- coding: utf-8 -*-
from openerp import api, models, fields

import base64

class adw_taskimport(models.Model):
    _inherit = "project.project"
	
    data_file = fields.Binary(
        'Bank Statement File', required=True,
        help='Get you bank statements in electronic format from your bank '
        'and select them here.')
		
    @api.multi
    def import_task(self):
        data_file = base64.b64decode(self.data_file)
		
    @api.model
    def _parse_file(self, data_file):
        """ Each module adding a file support must extends this method. It
        processes the file if it can, returns super otherwise, resulting in a
        chain of responsability.
        This method parses the given file and returns the data required by
        the bank statement import process, as specified below.
        - bank statements data: list of dict containing (optional
                                items marked by o) :
            -o currency code: string (e.g: 'EUR')
                The ISO 4217 currency code, case insensitive
            -o account number: string (e.g: 'BE1234567890')
                The number of the bank account which the statement
                belongs to
            - 'name': string (e.g: '000000123')
            - 'date': date (e.g: 2013-06-26)
            -o 'balance_start': float (e.g: 8368.56)
            -o 'balance_end_real': float (e.g: 8888.88)
            - 'transactions': list of dict containing :
                - 'name': string
                    (e.g: 'KBC-INVESTERINGSKREDIET 787-5562831-01')
                - 'date': date
                - 'amount': float
                - 'unique_import_id': string
                -o 'account_number': string
                    Will be used to find/create the res.partner.bank
                    in odoo
                -o 'note': string
                -o 'partner_name': string
                -o 'ref': string
        """
        raise Warning(_(
            'Could not make sense of the given file.\n'
            'Did you install the module to support this type of file?'
        ))		