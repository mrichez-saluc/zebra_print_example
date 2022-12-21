========================
Preciball Stock Scenario
========================

Imports::

    >>> import datetime
    >>> from decimal import Decimal
    >>> from proteus import Model, Wizard
    >>> from trytond.tests.tools import activate_modules
    >>> from trytond.modules.company.tests.tools import create_company, \
    ...     get_company
    >>> today = datetime.date.today()

Install preciball_stock::

    >>> config = activate_modules('preciball_stock')

Create company::

    >>> _ = create_company()
    >>> company = get_company()

Create product::

    >>> ProductUom = Model.get('product.uom')
    >>> ProductTemplate = Model.get('product.template')
    >>> unit, = ProductUom.find([('name', '=', 'Unit')])

    >>> template = ProductTemplate()
    >>> template.name = 'Product'
    >>> template.default_uom = unit
    >>> template.type = 'goods'
    >>> template.list_price = Decimal('20')
    >>> template.save()
    >>> product, = template.products

Get stock locations::

    >>> Location = Model.get('stock.location')
    >>> warehouse_loc, = Location.find([('code', '=', 'WH')])
    >>> supplier_loc, = Location.find([('code', '=', 'SUP')])
    >>> customer_loc, = Location.find([('code', '=', 'CUS')])
    >>> output_loc, = Location.find([('code', '=', 'OUT')])
    >>> storage_loc, = Location.find([('code', '=', 'STO')])

Create Lot::

    >>> Lot = Model.get('stock.lot')
    >>> lot = Lot(number='1234', product=product)
    >>> lot.save()

Fill storage::

    >>> StockMove = Model.get('stock.move')
    >>> incoming_move = StockMove()
    >>> incoming_move.product = product
    >>> incoming_move.lot = lot
    >>> incoming_move.uom = unit
    >>> incoming_move.quantity = 10
    >>> incoming_move.from_location = supplier_loc
    >>> incoming_move.to_location = storage_loc
    >>> incoming_move.planned_date = today
    >>> incoming_move.effective_date = today
    >>> incoming_move.company = company
    >>> incoming_move.unit_price = Decimal('100')
    >>> incoming_move.currency = company.currency
    >>> incoming_move.click('do')

List Locations Product Lot Quantity::

    >>> LotQuantityByLocation = Model.get('stock.lot.quantity.by.location')
    >>> lqbl, = LotQuantityByLocation.find([('product', '=', product)])
    >>> lqbl.location == storage_loc
    True
    >>> lqbl.quantity
    10.0
    >>> lqbl.lot.number
    u'1234'
