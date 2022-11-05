from django.urls import path
from . import views

urlpatterns = [
    path("myprofile", views.myprofile, name="myprofile"),
    path("edit/", views.edit, name="edit"),
    path("editprofile", views.editprofile, name='editprofile'),
]