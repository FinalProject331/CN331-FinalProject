from django.test import TestCase, Client
from django.shortcuts import render
from .models import Account
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.urls import reverse

class ChatViewsTestCase(TestCase):
    '''
    create user and create account
    '''
    def setUp(self):
        self.client = Client()
        password = make_password('password')
        self.user = User.objects.create(username='test', password=password)
        self.account = Account.objects.create(user=self.user)

    '''
    test view myprofile page
    '''
    def test_myprofile_view(self):
        self.client.login(username='test', password='password')
        response = self.client.get(reverse('myprofile'))
        self.assertEqual(response.status_code, 200)

    '''
    test view edit profile page
    '''
    def test_editprofile_view(self):
        self.client.login(username='test', password='password')
        response = self.client.get(reverse('editprofile'))
        
        self.assertEqual(response.status_code, 200)