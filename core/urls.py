from django.urls import path, include
from . import views
from chat.views import roomconfig
urlpatterns = [
    # path('', views.login, name='login'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('', views.home, name = "home"),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path('roomconfig', roomconfig, name='roomconfig'),

]