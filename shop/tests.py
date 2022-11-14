from django.test import TestCase, Client
from .models import Shop
from account.models import Account
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.urls import reverse

# Create your tests here.


class ShopTestCase(TestCase):
    '''
    make user with staff status
    create normal user
    make account to ready for use
    create object Shop with staff is user makeing before
    '''

    def setUp(self):
        self.client = Client()
        password = make_password('password')
        user = User.objects.create(username='staff', password=password)
        normal_user = User.objects.create(username="user",password=password)
        normal_account = Account.objects.create(user=normal_user)

        user.is_staff = True
        user.save()

        shop = Shop.objects.create(name="roomtest",staff=user)
        shop.save()

    '''
    login as staff user
    '''
    def test_staff_login(self):

        response = self.client.post(
            'home', {'username': 'staff', 'password': 'password'})
        self.assertTrue(response.status_code, 200)

    '''
    view the staff's shop
    '''
    def test_view_myshop(self):
        self.client.login(username='staff', password='password')
        response = self.client.get(reverse('myshop'))
        self.assertEqual(response.status_code, 200)

    '''
    view the modify staff's shop page
    '''
    def test_view_modify_myshop(self):
        self.client.login(username='staff', password='password')
        response = self.client.get(reverse('modifyshop'))
        self.assertEqual(response.status_code, 200)

    '''
    staff can modify staff's shop page
    '''
    def test_modify_myshop(self):
        self.client.login(username='staff', password='password')
        form = {'name': 'shop name', 'bio' : 'my shop detail', 'shopimg': 'defaultStaff.png'}
        response = self.client.get(reverse('modify'), form)
        self.assertEqual(response.status_code, 302)

    '''
    staff can upload myshop image
    '''
    def test_shop_upload(self):
        self.client.login(username='staff', password='password')
        form = {'shopimg': 'defaultStaff.png'}
        response = self.client.get(reverse('shopupload'), form)
        self.assertEqual(response.status_code, 302)
    '''
    view the staff help form
    '''
    def test_view_help(self):
        self.client.login(username='staff', password='password')
        response = self.client.get(reverse('help'))
        self.assertEqual(response.status_code, 200)
 
    '''
    staff can sent help form
    '''
    def test_send_help(self):
        self.client.login(username='staff', password='password')
        form = {'help_send': 'this is my report'}
        response = self.client.get(reverse('help_send'), form)
        self.assertEqual(response.status_code, 302)

    '''
    normal user can sent help form
    '''
    def test_normal_send_help(self):
        self.client.login(username='user', password='password')
        form = {'help_send': 'this is my report'}
        response = self.client.get(reverse('help_send'), form)
        self.assertEqual(response.status_code, 302)
    '''
    login normal user
    view shop list
    '''
    def test_user_view_shoplist(self):
        self.client.login(username='user', password='password')
        response = self.client.get(reverse('shoplist'))
        self.assertEqual(response.status_code, 200)

    '''
    login normal user
    view add shop page
    '''
    def test_view_add_shop(self):
        self.client.login(username='user', password='password')
        response = self.client.get(reverse('add_shop'))
        self.assertEqual(response.status_code, 200)

        '''
    normal user can sent add shop form
    '''
    def test_normal_send_help(self):
        self.client.login(username='user', password='password')
        form = {'add_shop_send': 'this is my form'}
        response = self.client.get(reverse('add_shop_send'), form)
        self.assertEqual(response.status_code, 302)
