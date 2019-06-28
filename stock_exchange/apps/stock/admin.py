from django.contrib import admin

from stock_exchange.apps.stock.models import Currency, Transactions


class CurrencyAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'current_value',
        'description'
    ]


class TransactionsAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'currency',
        'option',
        'transaction_amount',
        'transaction_date'
    ]

admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Transactions, TransactionsAdmin)