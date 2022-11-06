from django.test import TestCase, Client
from django.shortcuts import render
from .models import Account
from django.contrib.auth.models import User

class ChatViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='test', first_name='first', last_name='last', email='test@user.com')
        self.account = Account.objects.create(user=self.user)

    def test_myprofile_view(self):
        response = render(self.client, 'account/myprofile.html',{
            "account" : self.account})
        self.assertEqual(response.status_code, 200)

    # def test_editprofile_view(self):
    #     response = self.client.get('editprofile')
    #     self.assertEqual(response.status_code, 200)

    def test_edit_view(self):
        username = 'newUsername'
        self.user.username = username
        self.user.save()
        self.user.refresh_from_db()
        self.account.user = self.user
        self.account.save()
        self.account.refresh_from_db()
        response = render(self.client, 'account/myprofile.html')
        self.assertEqual(response.status_code, 200)