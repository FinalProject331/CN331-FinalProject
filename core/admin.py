from django.contrib import admin

# Register your models here.

from .models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ("account","birthday")
    


admin.site.register(Account, AccountAdmin)