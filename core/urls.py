from django.urls import path
from . import views


urlpatterns = [
    # path('', views.login, name='login'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('help', views.help, name='help'),
    
    path('', views.home, name = "home"),
    path("signup/", views.SignUp.as_view(), name="signup"),
]