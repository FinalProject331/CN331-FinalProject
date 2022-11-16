from django.test import TestCase, Client
from .models import Account
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.urls import reverse

# Create your tests here.

class AccountTestCase(TestCase):
    '''
    make user and Account for user
    '''
    def setUp(self):
        self.client = Client()
        password = make_password('password')
        self.user = User.objects.create(username='test', password=password)
        self.account = Account.objects.create(user=self.user)
    
    '''
    test user can edit yourself a profile
    '''
    def test_edit_profile(self):
        self.client.login(username='test', password='password')
        form = {'first_name' : "myfirstname", 'last_name' : "mylastname",
        'email' : "email@me.com", 'bio' : "this is my bio", 'username' : "username"}
        response = self.client.get(reverse('edit'), form)
        self.assertEqual(response.status_code, 302)

    '''
    test upload yorself a profile image success
    '''
    def test_upload_profile_success(self):
        self.client.login(username='test', password='password')
        form = {'image':"default.jpg"}

        response = self.client.post(reverse('upload'), form)
        self.assertEqual(response.status_code, 302)

    '''
    test upload yorself a profile image fail
    '''
    def test_upload_profile_fail(self):
        self.client.login(username='test', password='password')
        form = {'image':"default.jpg"}

        response = self.client.get(reverse('upload'), form)
        self.assertEqual(response.status_code, 200)



    def test_account_content(self):
        self.assertEqual(self.account.user, self.user)

    def test_update_account_chat(self):
        self.account.chat = 5
        self.assertEqual(self.account.chat, 5)

    def test_invalid_update_account_chat(self):
        self.account.chat = -1
        self.assertFalse(self.account == -1)


