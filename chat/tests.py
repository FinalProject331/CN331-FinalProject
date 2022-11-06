from django.test import TestCase, Client
from django.urls import reverse
from .models import Room, Message
from account.models import Account

# Create your tests here.

class ChatTestCase(TestCase):
    def setUp(self):
        self.room1 = Room.objects.create(name='test', max_seat=4)
        self.message = Message.objects.create(value='message1', user='test', room='room1')

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

class ChatViewsTestCase(TestCase):
    def setUp(self):
        room1 = Room.objects.create(name='test')

    def test_roomconfig_view(self):
        c = Client()
        response = c.get(reverse('roomconfig'))
        self.assertEqual(response.status_code, 200)
