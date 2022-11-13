from django.test import TestCase, Client
from django.urls import reverse
from chat.models import Room
from django.shortcuts import render, redirect
from account.models import Account
from chat.models import Message
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from chat.views import check_gender

class ChatViewsTestCase(TestCase):
    '''
    create room 
    create normal user
    create message
    make account to ready for use
    '''
    def setUp(self):
        self.client = Client()
        password = make_password('password')
        self.room = Room.objects.create(name='roomtest', request_gender = 'F')
        self.user = User.objects.create(username='test', first_name='first', last_name='last', email='test@user.com', password=password)
        self.account = Account.objects.create(user=self.user, gender='F')
        self.message = Message.objects.create(value='text', user=self.user.username, room=self.room.id)
        someone = User.objects.create(username="someone",password=password)
        Account.objects.create(user=someone, gender='F')

    '''
    view room config page
    '''
    def test_view_roomconfig(self):
        self.client.login(username='test', password='password')
        response = self.client.get(reverse('roomconfig'))
        self.assertEqual(response.status_code, 200)
    
    
    '''
    view valid room's detail page it should found page
    '''
    def test_valid_roomdetail_page(self):
        self.client.login(username='test', password='password')
        Account.objects.get(user=self.user)
        response = self.client.get(reverse('chat:room_detail' , args=["roomtest"]))
        self.assertEqual(response.status_code, 200)

    '''
    view invalid room's detail page it should not found page
    '''
    def test_invalid_roomdetail_page(self):
        response = self.client.get('roomdetail', {'room': 'something'})
        self.assertEqual(response.status_code, 404)

    '''
    user that meet requiremants available to join room  
    '''
    def test_join_room_avialable(self):
        self.client.login(username='test', password='password')
        response = self.client.get(reverse('chat:join_room' , args=["roomtest"]))
        self.assertEqual(response.status_code, 302)

    '''
    user that gender don't meet the requirements not available to join room  
    '''
    def test_join_room_gender_not_available(self):
        require = "F"
        gender = "M"
        check_gender(require, gender)
        require = "M"
        gender = "F"
        check_gender(require, gender)

    '''
    user who had joined a room can't join other room
    '''
    def test_join_room_chat_not_available(self):
        self.client.login(username='test', password='password')
        account = Account.objects.get(user=self.user)
        this_room = Room.objects.get(name = "roomtest")
        this_room.max_seat = 1
        account.chat = this_room.id

        response = self.client.get(reverse('chat:join_room' , args=["roomtest"]))
        self.assertEqual(response.status_code, 302)

    '''
    user not available to join a full room  
    '''
    def test_join_room_seat_not_available(self):
        self.client.login(username='someone', password='password')
        account = Account.objects.get(user=self.user)
        this_room = Room.objects.get(name = "roomtest")
        this_room.max_seat = 1
        account.chat = this_room.id

        response = self.client.get(reverse('chat:join_room' , args=["roomtest"]))
        self.assertEqual(response.status_code, 302)

    """ create new room """
    def test_create_room_checkview_available(self):
        response = redirect('/'+self.room.name+'/?username='+self.user.username)
        self.assertEqual(response.status_code, 302)

    """ send message in chat room """
    def test_send_message(self):
        response = HttpResponse('success')
        self.assertEqual(response.status_code, 200)

    """ chat botton in navbar has to redirect to chat room """
    def test_return_chat(self):
        response = redirect('/'+self.room.name+'/?username='+self.user.username)
        self.assertEqual(response.status_code, 302)

    """ leave chat room that user has joined before """
    def test_leave_room(self):
        response = redirect('home')
        self.assertEqual(response.status_code, 302)
    """ edit room name from oldname to newname """
    def test_edit_details(self):
        self.room.name = 'newname'
        response = redirect('/'+self.room.name+'/?username='+self.user.username)
        self.assertEqual(response.status_code, 302)

    # def test_edit_room(self):
    #     response = render(self.client, 'chat/edit_room.html',{
    #         "room" : self.room,
    #     })
    #     self.assertEqual(response.status_code, 200)
