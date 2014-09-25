# This file is part of the account_invoice_default_invoicing module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .configuration import *
from .invoice import *

def register():
    Pool.register(
        AccountConfiguration,
        Invoice,
        module='account_invoice_default_invoicing', type_='model')
