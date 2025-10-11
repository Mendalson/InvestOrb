from django.contrib import admin

from .models import Broker, Account, Security, Transaction, Position


admin.site.register(Broker)
admin.site.register(Account)
admin.site.register(Security)
admin.site.register(Transaction)
admin.site.register(Position)
