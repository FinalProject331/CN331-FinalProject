from django.urls import path
from . import views
app_name = 'chat'
urlpatterns = [
    # path('roomconfig', views.roomconfig, name='roomconfig'),
    path('<str:room>/', views.room, name='room'),
    path('join_room/<str:room>/', views.join_room, name='join_room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]