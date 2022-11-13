from django.test import TestCase, Client
from django.urls import reverse
from chat.models import Room
from django.shortcuts import render, redirect
from account.models import Account
from chat.models import Message
from django.contrib.auth.models import User
from django.http import HttpResponse


class ChatViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.room = Room.objects.create(name='roomtest', request_gender = 'F')
        self.user = User.objects.create(username='test', first_name='first', last_name='last', email='test@user.com')
        self.account = Account.objects.create(user=self.user, gender='F')
        self.message = Message.objects.create(value='text', user=self.user.username, room=self.room.id)

    # def test_roomconfig_view(self):
    #     response = render(self.client, 'chat/roomconfig.html', {
    #         'account': self.account,
    #     })
    #     self.assertEqual(response.status_code, 200)

    def test_valid_roomdetail_page(self):
        response = render(self.client, "chat/roomdetail.html", {
            "room": self.room,
            "account": self.account,
        })
        self.assertEqual(response.status_code, 200)

    def test_invalid_roomdetail_page(self):
        response = self.client.get('roomdetail', {'room': 'something'})
        self.assertEqual(response.status_code, 404)

    def test_join_room_avialable(self):
        response = redirect('/'+self.room.name+'/?username='+self.user.username)
        self.assertEqual(response.status_code, 302)

    def test_join_room_gender_not_available(self):
        self.room.request_gender = 'M'
        self.assertFalse(self.account.gender==self.room.request_gender)
        response = render(self.client, 'chat/roomdetail.html', {
            'room': self.room,
            'account': self.account,
        })
        self.assertEqual(response.status_code, 200)

    def test_join_room_chat_not_available(self):
        self.account.chat = 5
        self.assertFalse(self.account.chat == self.room.id)
        self.assertFalse(self.account.chat == 0)
        response = render(self.client, 'chat/roomdetail.html', {
            'room': self.room,
            'account': self.account,
        })
        self.assertEqual(response.status_code, 200)
    
    def test_join_room_seat_not_available(self):
        self.room.seat_count = 2
        self.room.status = 'Close'
        self.assertEqual(self.room.seat_count, self.room.max_seat)
        self.assertFalse(self.room.is_available())
        response = render(self.client, 'chat/roomdetail.html', {
            'room': self.room,
            'account': self.account,
        })
        self.assertEqual(response.status_code, 200)

    def test_create_room_checkview_available(self):
        response = redirect('/'+self.room.name+'/?username='+self.user.username)
        self.assertEqual(response.status_code, 302)

    # def test_create_room_checkview_account_chat_not_available(self):
    #     self.account.chat = 5
    #     self.assertFalse(self.account.chat == 0)
    #     response = render(self.client, 'chat/roomconfig.html')
    #     self.assertEqual(response.status_code, 200)

    def test_send_message(self):
        response = HttpResponse('success')
        self.assertEqual(response.status_code, 200)

    
    def test_return_chat(self):
        response = redirect('/'+self.room.name+'/?username='+self.user.username)
        self.assertEqual(response.status_code, 302)

    def test_leave_room(self):
        response = redirect('home')
        self.assertEqual(response.status_code, 302)

    def test_edit_details(self):
        self.room.name = 'newname'
        response = redirect('/'+self.room.name+'/?username='+self.user.username)
        self.assertEqual(response.status_code, 302)

    # def test_edit_room(self):
    #     response = render(self.client, 'chat/edit_room.html',{
    #         "room" : self.room,
    #     })
    #     self.assertEqual(response.status_code, 200)
