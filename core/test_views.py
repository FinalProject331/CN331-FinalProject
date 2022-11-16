from django.test import TestCase, Client
from django.urls import reverse
from account.models import Account
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.urls import reverse
# Create your tests here.

# views_test

class CoreViewsTestCase(TestCase):

    '''
    create user and create account
    '''
    def setUp(self):
        self.client = Client()
        password = make_password('password')
        self.user = User.objects.create(username='test', password=password)
        self.account = Account.objects.create(user=self.user)

    def test_aboutus_view(self):
        response = self.client.get(reverse('aboutus'))
        self.assertEqual(response.status_code, 200)

    def test_help_view(self):
        response = self.client.get(reverse('help'))
        self.assertEqual(response.status_code, 200)

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_signup_view(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_valid_createuser(self):
        response = self.client.get('login', {'username': 'test', 'password': 'test1234',
         'first_name': 'first', 'last_name': 'last', 'email': 'test@user.com'})
        self.assertTrue(response.status_code, 200)
    
class LogInViewTest(TestCase):

    def setUp(self):
        self.user = {
            'username': 'test',
            'password': 'test1234'}
        User.objects.create_user(self.user)

    def test_valid_login(self):
        c = Client()
        response = c.post('home', {'username': 'test', 'password': 'test1234'})
        self.assertTrue(response.status_code, 200)

    def test_invalid_login(self):
        c = Client()
        response = c.post('login', {'username': 'test', 'password': 'wrong'})
        self.assertTrue(response.status_code, 404)

    def test_logout(self):
        c = Client()
        response = c.post('login', {'username': 'test', 'password': 'test1234'})
        self.assertTrue(response.status_code, 200)
        c.logout()
        response = c.get(reverse('login'))
        self.assertEqual(response.status_code, 200)