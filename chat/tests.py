from django.test import TestCase, Client
from .models import Room, Message
from account.models import Account
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.urls import reverse
from datetime import datetime
# from datetime import timedelta as timeobj

# Create your tests here.


class ChatTestCase(TestCase):

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
        room = Room.objects.create(name='roomtest', request_gender='F', max_seat = 2)

        # create user 1
        test1 = User.objects.create(username='test1', first_name='first',
                                    last_name='last', email='test@user.com', password=password)
        testaccount1 = Account.objects.create(user=test1, gender='F')

        # create user 2
        test2 = User.objects.create(username="test2", password=password)
        testaccount2 = Account.objects.create(user=test2, gender='F')

        # create Message
        self.message = Message.objects.create(
            value='text', user=test1, room=room.id)

    """
    test view room by url directly
    """
    def test_join_room_user_directly_valid(self):
        self.client.login(username='test1', password='password')
        user = User.objects.get(username="test1")
        room = Room.objects.get(name="roomtest")
        response = self.client.get(
            '/'+str(room.id)+'/?username='+user.username, args=[str(room.id)])
        self.assertEqual(response.status_code, 200)

    '''
    action join room
    user that meet requirements available to join room  
    '''
    def test_join_room_avialable(self):
        self.client.login(username='test1', password='password')
        response = self.client.get(reverse('chat:join_room' , args=[1]))
        self.assertEqual(response.status_code, 302)

    '''
    action join room
    test join room same as last join 
    '''
    def test_join_room_last(self):
        self.client.login(username='test1', password='password')
        user = User.objects.get(username="test1")
        account = Account.objects.get(user=user)
        room = Room.objects.get(name="roomtest")
        account.chat = room.id
        account.save()
        response = self.client.get(reverse('chat:join_room' , args=[1]))
        self.assertEqual(response.status_code, 302)

    '''
    action join room
    user who had joined a room can't join other room
    '''
    def test_join_room_chat_not_available(self):
        self.client.login(username='test1', password='password')
        user = User.objects.get(username="test1")
        account = Account.objects.get(user=user)
        room = Room.objects.get(name="roomtest")
        room2 = Room.objects.create(name="the_room", max_seat = 2)
        account.chat = room.id
        account.save()
        response = self.client.get(reverse('chat:join_room' , args=[room2.id]))
        self.assertEqual(response.status_code, 200)

    '''
    action join room
    user not available to join a full room  
    '''
    def test_join_room_seat_not_available(self):
        # login user test 2
        self.client.login(username='test2', password='password')

        # make user test 1 in room test
        user = User.objects.get(username="test1")
        account = Account.objects.get(user=user)
        room = Room.objects.get(name="roomtest")
        account.chat = room.id
        account.gender = "F"
        account.save()

        # set max seat, and requirement
        room.max_seat = 1
        room.request_gender = "F"
        room.save()

        # join full room
        response = self.client.get(reverse('chat:join_room' , args=[room.id]))
        self.assertEqual(response.status_code, 200)

    '''
    action join room
    test join with wrong gender require 
    '''
    def test_chat_join_invalid_gender_require(self):
        # login user test 1
        self.client.login(username='test1', password='password')
        user = User.objects.get(username="test1")
        account = Account.objects.get(user=user)
        account.chat = 0
        account.gender = "M"
        account.save()

        # set max seat, and requirement
        room = Room.objects.get(name="roomtest")
        room.max_seat = 7
        room.request_gender = "F"
        room.save()

        # join invalid require
        response = self.client.get(reverse('chat:join_room' , args=[room.id]))
        self.assertEqual(response.status_code, 200)

    '''
    action check view
    case success
    '''
    def test_chat_checkview_success(self):
        self.client.login(username='test1', password='password')
        longtime = datetime(2222,12,31,23,59,59)
        form = {'room_name':"somename", 'description':"my description", 'max_seat':"3",
        'gender_request':'N', 'dead_time': longtime, 'meal_time':longtime
        }

        response = self.client.post(reverse('chat:checkview'), form)
        self.assertEqual(response.status_code, 302)
 
    '''
    action check view
    case fail already in some room
    '''
    def test_chat_checkview_already_join_room(self):
        self.client.login(username='test1', password='password')
        user = User.objects.get(username="test1")
        account = Account.objects.get(user=user)
        account.chat = 1
        account.gender = "M"
        account.save()
        longtime = datetime(2222,12,31,23,59,59)
        form = {'room_name':"somename", 'description':"my description", 'max_seat':"3",
        'gender_request':'N', 'dead_time': longtime, 'meal_time':longtime
        }

        response = self.client.post(reverse('chat:checkview'), form)
        self.assertEqual(response.status_code, 200)

    '''
    action check view
    case fail invalid form
    '''
    def test_chat_checkview_invalid_form(self):
        self.client.login(username='test1', password='password')
        user = User.objects.get(username="test1")
        account = Account.objects.get(user=user)
        account.chat = 0
        account.gender = "M"
        account.save()
        time = datetime(2000,12,31,23,59,59)
        form = {'room_name':"somename", 'description':"my description", 'max_seat':"3",
        'gender_request':'N', 'dead_time': time, 'meal_time': time
        }

        response = self.client.post(reverse('chat:checkview'), form)
        self.assertEqual(response.status_code, 200)

    '''
    user test send message
    '''
    def test_send_message(self):
        self.client.login(username='test1', password='password')
        form = {'message':"test some thing", 'username':'test1', 'room_id':1}
        response = self.client.post(reverse('chat:send'), form)
        self.assertEqual(response.status_code, 200)

    '''
    user get message
    '''
    def test_getmessage(self):
        self.client.login(username='test1', password='password')
        room = Room.objects.get(name="roomtest")
        response = self.client.post(reverse('chat:getMessages', args=[room.id]))
        self.assertEqual(response.status_code, 200)

    '''
    test return to former chat room
    '''
    def test_return_to_former_chat(self):
        self.client.login(username='test1', password='password')
        user = User.objects.get(username="test1")
        account = Account.objects.get(user=user)
        room = Room.objects.get(name="roomtest")
        account.chat = room.id
        account.save()

        response = self.client.get(reverse('chat:return_chat' , args=[room.id]))
        self.assertEqual(response.status_code, 302)

    '''
    test action leave room
    '''
    def test_chat_leave_room(self):
        self.client.login(username='test1', password='password')

        # user join room
        user = User.objects.get(username="test1")
        account = Account.objects.get(user=user)
        room = Room.objects.get(name="roomtest")
        room.max_seat = 7
        account.chat = room.id
        account.save()

        response = self.client.get(reverse('chat:leave_room' , args=[room.id]))
        self.assertEqual(response.status_code, 302)

    '''
    test user edit room detail
    '''
    def test_chat_edit_room_with_details(self):
        self.client.login(username='test1', password='password')

        # user join room
        user = User.objects.get(username="test1")
        account = Account.objects.get(user=user)
        room = Room.objects.get(name="roomtest")
        room.max_seat = 7
        account.chat = room.id
        account.save()
        
        longtime = datetime(2099,12,31,23,59,59)
        form = {'room_name':"somename", 'description':"my description", 'max_seat':"3",
        'gender_request':'N', 'dead_time': longtime, 'meal_time':longtime, 'status':'C'
        }
        response = self.client.post(reverse('chat:edit_details' , args=[room.id]), form)
        self.assertEqual(response.status_code, 302)