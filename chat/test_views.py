from django.test import TestCase, Client
from django.urls import reverse
from chat.models import Room
from datetime import datetime
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
    test view edit room page 
    '''
    def test_chat_view_edit_room(self):
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
        response = self.client.post(reverse('chat:edit_room' , args=[room.id]), form)
        self.assertEqual(response.status_code, 200)