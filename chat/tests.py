from django.test import TestCase, Client
from django.urls import reverse
from .models import Room, Message

# Create your tests here.

class ChatModelsTestCase(TestCase):
    def setUp(self):
        self.room1 = Room.objects.create(name='test')
        # self.room1 = Room.objects.create(name='test', max_seat=2)
        self.message = Message.objects.create(value='message1', user='test', room='room1')

    def test_read_message(self):
        self.assertEqual(self.room1.name, self.message.user)
        # self.assertEqual(self.message.value, 'message1')

    # def test_update_max_seat(self):
    #     self.room1.max_seat = 4
    #     self.assertEqual(self.room1.max_seat, 4)
