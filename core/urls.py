from django.urls import path
from . import views
from chat.views import roomconfig


urlpatterns = [
    path('aboutus', views.aboutus, name='aboutus'),
    path('help', views.help, name='help'),
    path('help_send', views.help_send, name='help_send'),
    path('', views.home, name = "home"),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path('roomconfig', roomconfig, name='roomconfig'),
]