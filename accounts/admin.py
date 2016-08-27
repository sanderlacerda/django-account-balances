from django.contrib import admin
from treebeard.admin import TreeAdmin

from accounts import models


class AccountAdmin(admin.ModelAdmin):
    list_display = ['id', 'address', 'code', 'name', 'balance', 'credit_limit', 'primary_user',
                    'start_date', 'end_date', 'is_active',
                    'date_created', 'currency']
    readonly_fields = ('balance', 'code',)


class TransferAdmin(admin.ModelAdmin):
    list_display = ['reference', 'amount_from', 'amount_to', 'source', 'destination',
                    'user', 'description', 'date_created', 'exchange', 'currency_from', 'currency_to']
    readonly_fields = ('amount_from', 'amount_to', 'source', 'destination', 'description',
                       'user', 'username', 'date_created')

class TransactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'transfer', 'account', 'amount_from', 'amount_to', 'exchange_rate', 'date_created']
    readonly_fields = ('transfer', 'account', 'amount_from', 'amount_to', 'exchange_rate', 'date_created')


class IPAddressAdmin(admin.ModelAdmin):
    list_display = ['ip_address', 'total_failures', 'consecutive_failures',
                    'is_temporarily_blocked', 'is_permanently_blocked',
                    'date_last_failure']
    readonly_fields = ('ip_address', 'total_failures', 'date_last_failure')


admin.site.register(models.AccountType, TreeAdmin)
admin.site.register(models.Account, AccountAdmin)
admin.site.register(models.Transfer, TransferAdmin)
admin.site.register(models.Transaction, TransactionAdmin)
admin.site.register(models.IPAddressRecord, IPAddressAdmin)
