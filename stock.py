# The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from io import BytesIO

import barcode
from barcode.writer import ImageWriter

from trytond.model import fields
from trytond.modules.zebra_print.zebra import ZebraReport
from trytond.pool import Pool, PoolMeta
from trytond.pyson import Eval
from trytond.transaction import Transaction


class Lot(metaclass=PoolMeta):
    __name__ = "stock.lot"
    id_supplier_pallet = fields.Char("Id Supplier Pallet")
    barcode = fields.Function(fields.Binary("Barcode",
        states={
            'invisible': ~Eval('barcode'),
            }), 'get_barcode')

    def get_barcode(self, name):
        fd = BytesIO()
        barcode.generate(
            'code128', str(self.number),
            writer=ImageWriter(), output=fd)
        fd.seek(0)
        return fields.Binary.cast(fd.read())


class ZebraLabelStockLot(ZebraReport):
    'Zebra Label'
    __name__ = 'stock.lot.zebra.xml'

    @classmethod
    def execute(cls, ids, data):
        User = Pool().get('res.user')
        user = User(Transaction().user)
        zebra_printer = getattr(user, 'zebra_printer', None)

        with Transaction().set_context(
                printer_hostname=zebra_printer):
            return super().execute(ids, data)
