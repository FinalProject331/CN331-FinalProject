from django.urls import path
from . import views
app_name = 'chat'
urlpatterns = [
    # path('roomconfig', views.roomconfig, name='roomconfig'),
    path('<int:room>/', views.room, name='id'),
    path('join_room/<int:room>/', views.join_room, name='join_room'),
    path('checkview', views.checkview, name='checkview'),
    # path('create_room', views.create_room, name='create_room'),
    path('send', views.send, name='send'),
    path('getMessages/<int:room>/', views.getMessages, name='getMessages'),
    path('room_detail/<int:room>/', views.room_detail, name='room_detail'),
    path('return_chat/<int:chat>/', views.return_chat, name='return_chat'),
    path('leave_room/<int:room>/', views.leave_room, name='leave_room'),
    path('<str:room>/edit_details', views.edit_details, name='edit_details'),
    path('<str:room>/edit_room', views.edit_room, name='edit_room'),
]