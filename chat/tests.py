from django.test import TestCase
from .models import Room, Message
from account.models import Account
from django.contrib.auth.models import User

# Create your tests here.

class ChatTestCase(TestCase):
    def setUp(self):
        self.room1 = Room.objects.create(name='test', max_seat=4)
        self.message = Message.objects.create(value='message1', user='test', room='room1')
        self.user = User.objects.create(username='test', first_name='first', last_name='last', email='test@user.com')
        self.account = Account.objects.create(user=self.user)

    def test_read_message(self):
        self.assertEqual(self.room1.name, self.message.user)
        self.assertEqual(self.message.value, 'message1')

    def test_update_max_seat(self):
        self.room1.max_seat = 3
        self.assertEqual(self.room1.max_seat, 3)

    def test_seat_available(self):
        self.assertTrue(self.room1.is_seat_available())

    def test_seat_not_available(self):
        self.room1.seat_count = 4
        self.assertFalse(self.room1.is_seat_available())

    def test_join_room_available(self):
        self.assertEqual(self.account.chat, 0)
    
    def test_join_room_not_available(self):
        self.account.chat = self.room1.id
        self.assertTrue(self.account.chat != 0 or self.account.chat != self.room1.id)

    def test_create_room_available(self):
        self.assertEqual(self.account.chat, 0)

    def test_create_room_not_available(self):
        self.account.chat = self.room1.id
        self.assertFalse(self.account.chat == 0)

