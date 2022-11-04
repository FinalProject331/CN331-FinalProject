from django.urls import path
from . import views

urlpatterns = [
    path("myprofile", views.myprofile, name="myprofile"),
    
    path("editprofile", views.editprofile, name='editprofile'),
]