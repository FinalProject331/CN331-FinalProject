from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("myprofile", views.myprofile, name="myprofile"),
    path("edit/", views.edit, name="edit"),
    path("editprofile", views.editprofile, name='editprofile'),
    
]