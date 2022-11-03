<<<<<<< HEAD
from django.urls import path, include
=======
import imp
from django.urls import path
from chat.views import room
>>>>>>> cc0a395 (test room)
from . import views
from chat.views import roomconfig
urlpatterns = [
    # path('', views.login, name='login'),
    path('aboutus', views.aboutus, name='aboutus'),
    
    path('signup/create_user', views.create_user, name='create_user'),
    # path('home', views.home, name='home'),
    path('', views.home, name = "home"),
    path("signup/", views.SignUp.as_view(), name="signup"),
<<<<<<< HEAD
    path('roomconfig', roomconfig, name='roomconfig'),

=======
    path('<str:room>/', room, name='room'),
>>>>>>> cc0a395 (test room)
]