from django.contrib import admin

# Register your models here.
from .models import User, Accounts, ID_CARD
admin.site.register(User)
admin.site.register(Accounts)
admin.site.register(ID_CARD)