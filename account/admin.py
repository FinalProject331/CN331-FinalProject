from django.contrib import admin

from .models import Account

# Register your models here.

# class AccountAdmin(admin.ModelAdmin):
#     list_display = ("account","birthday")
    


# admin.site.register(Account, AccountAdmin)
admin.site.register(Account)