from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("myshop/", views.myshop, name="myshop"),
    path("modify/", views.modify, name="modify"),
    path("modifyshop", views.modifyshop, name='modifyshop'),
    path("uploadshop/", views.uploadshop, name="uploadshop"),
    path("search_shop/", views.search_shop, name='search_shop'),
    path("shoplist", views.shoplist, name="shoplist"),
    path("add_shop", views.add_shop, name="add_shop"),
    path("add_shop_send", views.add_shop_send, name="add_shop_semd"),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)