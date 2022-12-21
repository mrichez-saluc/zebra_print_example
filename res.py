# The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta


class User(metaclass=PoolMeta):
    __name__ = 'res.user'

    zebra_printer = fields.Char("Zebra Printer",
        help="The default zebra printer for printing labels.")

    @classmethod
    def __setup__(cls):
        super().__setup__()
        cls._preferences_fields.append('zebra_printer')

    @classmethod
    def _get_preferences(cls, user, context_only=False):
        preferences = super()._get_preferences(user, context_only=context_only)
        if user.zebra_printer:
            preferences['zebra_printer'] = user.zebra_printer
        return preferences
