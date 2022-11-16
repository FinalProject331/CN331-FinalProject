from django.test import TestCase, Client
from django.urls import reverse
from chat.models import Room
from django.shortcuts import render, redirect
from account.models import Account
from chat.models import Message
from django.contrib.auth.models import User
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

        # create room
        room = Room.objects.create(name='roomtest', request_gender = 'F')

        # create user 1
        test1 = User.objects.create(username='test1', first_name='first', last_name='last', email='test@user.com', password=password)
        testaccount1 = Account.objects.create(user=test1, gender='F')

        # create user 2
        test2 = User.objects.create(username="test2",password=password)
        testaccount2 = Account.objects.create(user=test2, gender='F')

        # create Message
        self.message = Message.objects.create(value='text', user=test1, room=room.id)

    '''
    view room config page
    '''
    def test_view_roomconfig(self):
        self.client.login(username='test1', password='password')
        response = self.client.get(reverse('roomconfig'))
        self.assertEqual(response.status_code, 200)
    
    
    '''
    view valid room's detail page it should found page
    '''
    def test_valid_roomdetail_page(self):
        self.client.login(username='test1', password='password')
        room = Room.objects.get(name ="roomtest")
        user = User.objects.get(username="test1")
        Account.objects.get(user=user)
        response = self.client.get(reverse('chat:room_detail' , args=[room.id]))
        self.assertEqual(response.status_code, 200)

    '''
    view invalid room's detail page it should not found page
    '''
    def test_invalid_roomdetail_page(self):
        
        response = self.client.get('roomdetail', {'room': 'something'})
        self.assertEqual(response.status_code, 404)

    # '''
    # test view chat page
    # '''
    # def test_view_room(self):
    #     self.client.login(username='test1', password='password')
    #     response = self.client.get("\1\?username=test1")
    #     self.assertEqual(response.status_code, 302)

    """
    action join room
    """
    '''
    user that meet requiremants available to join room  
    '''
    def test_join_room_avialable(self):
        self.client.login(username='test1', password='password')
        response = self.client.get(reverse('chat:join_room' , args=[1]))
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

    # '''
    # user who had joined a room can't join other room
    # '''
    # def test_join_room_chat_not_available(self):
    #     self.client.login(username='test1', password='password')
    #     account = Account.objects.get(user=self.user)
    #     this_room = Room.objects.get(name = "roomtest")
    #     this_room.max_seat = 1
    #     account.chat = this_room.id

    #     response = self.client.get(reverse('chat:join_room' , args=[1]))
    #     self.assertEqual(response.status_code, 302)

    # '''
    # user not available to join a full room  
    # '''
    # def test_join_room_seat_not_available(self):
    #     self.client.login(username='test2', password='password')
    #     account = Account.objects.get(user=self.user)
    #     this_room = Room.objects.get(name = "roomtest")
    #     this_room.max_seat = 1
    #     account.chat = this_room.id

    #     response = self.client.get(reverse('chat:join_room' , args=[1]))
    #     self.assertEqual(response.status_code, 302)

    '''
    test join room same as last join 
    '''
    def test_join_room_last(self):
        self.client.login(username='test2', password='password')
        user = User.objects.get(username="test2")
        account = Account.objects.get(user=user)
        account.chat = 1
        response = self.client.get(reverse('chat:join_room' , args=[1]))
        self.assertEqual(response.status_code, 302)


    # """ create new room """
    # def test_create_room_checkview_available(self):
    #     response = redirect('/'+self.room.id+'/?username='+self.user.username)
    #     self.assertEqual(response.status_code, 302)

    # """ send message in chat room """
    # def test_send_message(self):
    #     response = HttpResponse('success')
    #     self.assertEqual(response.status_code, 200)

    # """ chat botton in navbar has to redirect to chat room """
    # def test_return_chat(self):
    #     response = redirect('/'+self.room.id+'/?username='+self.user.username)
    #     self.assertEqual(response.status_code, 302)

    # """ leave chat room that user has joined before """
    # def test_leave_room(self):
    #     response = redirect('home')
    #     self.assertEqual(response.status_code, 302)
    # """ edit room name from oldname to newname """
    # def test_edit_details(self):
    #     self.room.name = 'newname'
    #     response = redirect('/'+self.room.id+'/?username='+self.user.username)
    #     self.assertEqual(response.status_code, 302)

    # def test_edit_room(self):
    #     response = render(self.client, 'chat/edit_room.html',{
    #         "room" : self.room,
    #     })
    #     self.assertEqual(response.status_code, 200)
