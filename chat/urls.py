from django.urls import path
from . import views
app_name = 'chat'
urlpatterns = [
    # path('roomconfig', views.roomconfig, name='roomconfig'),
    path('<str:room>/', views.room, name='room'),
    path('join_room/<str:room>/', views.join_room, name='join_room'),
    path('checkview', views.checkview, name='checkview'),
    # path('create_room', views.create_room, name='create_room'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    path('room_detail/<str:room>/', views.room_detail, name='room_detail'),
    path('return_chat/<str:chat>/', views.return_chat, name='return_chat'),
    path('leave_room/<str:room>/', views.leave_room, name='leave_room'),
    # path('edit_details', views.edit_details, name='edit_details'),
    path('edit_room/<str:room>/', views.edit_room, name='edit_room'),
]