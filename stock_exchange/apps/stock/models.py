from datetime import date

from django.db import models
from django.utils.translation import ugettext_lazy as _

from stock_exchange.apps.users.models import User
from .choices import MARKET_OPTIONS

class Currency(models.Model):
    # Name of currency
    name = models.CharField(_('Currency name'), max_length=50)

    # Storage cost in $ for currency
    current_value = models.DecimalField(_('Actual rate'), max_digits=30,
        decimal_places=5)

    # Storage description of currency
    description = models.TextField(_('Description'), blank=True, null=True)
    
    def __str__(self):
        return '{}'.format(self.name)


class Transaction(models.Model):
    # Identifies user which contains User model.
    user = models.ForeignKey(User, on_delete = models.CASCADE)

     # Identifies currency which contains Currency model.
    currency = models.ForeignKey(Currency, on_delete = models.CASCADE)

    # Storage type of transaction.
    option = models.CharField(_('Transaction option'), 
        choices = MARKET_OPTIONS, max_length=4)

    # Storage cost of currency.
    transaction_amount = models.DecimalField(_('Purchase cost'), max_digits=30,
        decimal_places=5)

    # Storage transaction date.
    transaction_date = models.DateField(_('Transaction date'), auto_now=True)