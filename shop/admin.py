from django.contrib import admin
from .models import Shop, ShopChat, AddShop, ShopMessage
# Register your models here.

admin.site.register(Shop)
admin.site.register(ShopChat)
admin.site.register(AddShop)
admin.site.register(ShopMessage)

