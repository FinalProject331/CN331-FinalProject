from django.test import TestCase, Client
from .models import Room, Message
from account.models import Account
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Create your tests here.

# class ChatTestCase(TestCase):

#     '''
#     create room 
#     create normal user
#     create message
#     make account to ready for use
#     '''
#     def setUp(self):
#         self.client = Client()
#         password = make_password('password')

#         # create room
#         room = Room.objects.create(name='roomtest', request_gender = 'F')

#         # create user 1
#         test1 = User.objects.create(username='test1', first_name='first', last_name='last', email='test@user.com', password=password)
#         testaccount1 = Account.objects.create(user=test1, gender='F')

#         # create user 2
#         test2 = User.objects.create(username="test2",password=password)
#         testaccount2 = Account.objects.create(user=test2, gender='F')

#         # create Message
#         self.message = Message.objects.create(value='text', user=test1, room=room.id)




