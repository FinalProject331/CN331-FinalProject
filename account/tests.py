from django.test import TestCase
from .models import Account
from django.contrib.auth.models import User

# Create your tests here.

class AccountTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test', first_name='first', last_name='last', email='test@user.com')
        self.account = Account.objects.create(user=self.user)
    
    def test_account_content(self):
        self.assertEqual(self.account.user, self.user)

    def test_update_account_chat(self):
        self.account.chat = 5
        self.assertEqual(self.account.chat, 5)

    # def test_invalid_update_account_chat(self):
    #     self.account = -1
    #     self.assertFalse(self.account == -1)
