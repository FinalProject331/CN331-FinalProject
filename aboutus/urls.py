from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name='login'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('signup', views.signup, name='signup'),
    path('signup/create_user', views.create_user, name='create_user'),
    path('home', views.home, name='home'),
]