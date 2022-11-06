from django.contrib.auth.models import User
from django.test import TestCase
from django.contrib.auth import authenticate

class LogInTest(TestCase):

    def setUp(self):
        self.user = {
            'username': 'test',
            'password': 'test1234'}
        User.objects.create_user(**self.user)
        
    def test_correct(self):
        user = authenticate(username='test', password='test1234')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='test1234')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_pssword(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)