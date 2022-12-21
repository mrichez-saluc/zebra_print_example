# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

try:
    from trytond.modules.preciball_stock.tests.test_preciball_stock import suite
except ImportError:
    from .test_preciball_stock import suite

__all__ = ['suite']
