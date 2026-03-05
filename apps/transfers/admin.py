from django.contrib import admin

# Register your models here.


from .models import Transaction, Transfer
admin.site.register(Transfer)
admin.site.register(Transaction)