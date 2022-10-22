from django.contrib import admin
from django.urls import path, include
import views

urlpatterns = [
    
    path('', views.aboutus(), name="aboutus")

]