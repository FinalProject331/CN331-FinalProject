from django.urls import path
from . import views
from chat.views import roomconfig
from shop.views import shoplist

urlpatterns = [
    path('aboutus', views.aboutus, name='aboutus'),
    path('help', views.help, name='help'),
    path('help_send', views.help_send, name='help_send'),
    path('', views.home, name = "home"),
    path("signup/", views.signup, name="signup"),
    path("signup/create_account", views.create_account, name="create_account"),
    path('roomconfig', roomconfig, name='roomconfig'),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("shoplist/", shoplist, name="shoplist"),
    path("search/", views.search, name='search'),
    path("filter", views.filter, name='filter'),
    path("joinable", views.joinable, name='joinable'),
]
