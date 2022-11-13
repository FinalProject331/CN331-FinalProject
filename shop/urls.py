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
    path("add_shop_send", views.add_shop_send, name="add_shop_send"),
    path("viewshop/<int:id>", views.viewshop, name="viewshop"),
    path('<str:room>/', views.shoproom, name='shoproom'),
    path('shopcheckview/<str:shop>', views.shopcheckview, name='shopcheckview'),
    path('shopsend', views.shopsend, name='shopsend'),
    path('shopgetMessages/<str:room>/', views.shopgetMessages, name='shopgetMessages'),
    path('join_chat/<str:chat>', views.join_chat, name="join_chat"),
    path("shopupload", views.shopupload, name="shopupload")
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)