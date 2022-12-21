# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.pool import Pool

from . import res
from . import stock


__all__ = ['register', 'routes']


def register():
    Pool.register(
        stock.Lot,
        res.User,
        module='zebra_exemple', type_='model')
    Pool.register(
    module='zebra_exemple', type_='wizard')
    Pool.register(
        stock.ZebraLabelStockLot,
        module='zebra_exemple', type_='report')
