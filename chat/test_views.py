from django.test import TestCase, Client
from django.urls import reverse
from chat.models import Room


class ChatViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.room = Room.objects.create(name='roomtest')

    def test_roomconfig_view(self):
        response = self.client.get(reverse('roomconfig'))
        self.assertEqual(response.status_code, 200)

    # def test_valid_roomdetail_page(self):
    #     response = self.client.get('roomdetail', {'room': 'roomtest'})
    #     self.assertEqual(response.status_code, 200)

    def test_invalid_roomdetail_page(self):
        response = self.client.get('roomdetail', {'room': 'something'})
        self.assertEqual(response.status_code, 404)
