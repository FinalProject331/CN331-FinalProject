from django.test import TestCase, Client
from django.urls import reverse
from account.models import Account
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.urls import reverse
from shop.models import Shop, ShopChat
from chat.models import Room
# Create your tests here.

# views_test

class CoreViewsTestCase(TestCase):

    '''
    create user and create account
    create staff and his shop
    create admin user
    create 2 room with name include empty
    '''
    def setUp(self):
        self.client = Client()
        password = make_password('password')

        # create user
        user = User.objects.create(username='test', password=password)
        account = Account.objects.create(user=user)
        
        # create admin
        admin = User.objects.create_superuser(username="admin", password =password)
        
        # create staff and his shop
        staff = User.objects.create(username='staff', password=password)
        staff.is_staff = True
        staff.save()
        shop = Shop.objects.create(name="roomtest",staff=staff)
        shop.save()

        #create room
        Room.objects.create(name="emptyroom")
        Room.objects.create(name="roomempty")

    '''
    views aboutus page as anonymous
    '''
    def test_aboutus_view_anonymous(self):
        c = Client()
        response = c.get(reverse('aboutus'))
        self.assertEqual(response.status_code, 200)
        
    '''
    views aboutus page as staff
    '''
    def test_aboutus_view_staff(self):
        self.client.login(username='staff', password='password')
        response = self.client.get(reverse('aboutus'))
        self.assertEqual(response.status_code, 200)
        
    '''
    views aboutus page as user
    '''
    def test_aboutus_view_user(self):
        self.client.login(username='test', password='password')
        response = self.client.get(reverse('aboutus'))
        self.assertEqual(response.status_code, 200)

    '''
    view help form page as anonymous
    '''
    def test_help_view_anonymous(self):
        c = Client()
        response = c.get(reverse('help'))
        self.assertEqual(response.status_code, 200)

    '''
    view help form page as staff
    '''
    def test_help_view_staff(self):
        self.client.login(username='staff', password='password')
        response = self.client.get(reverse('help'))
        self.assertEqual(response.status_code, 200)

    '''
    view help form page as user
    '''
    def test_help_view_user(self):
        self.client.login(username='test', password='password')
        response = self.client.get(reverse('help'))
        self.assertEqual(response.status_code, 200)

    '''
    view home page as anonymous
    '''
    def test_home_view_anonymous(self):
        c = Client()
        response = c.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    '''
    view home page as admin
    '''
    def test_home_view_admin(self):
        self.client.login(username='admin', password='password')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    '''
    view home page as staff
    '''
    def test_home_view_staff(self):

        self.client.login(username='staff', password='password')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        
    '''
    view home page as user
    '''
    def test_home_view_user(self):
        self.client.login(username='test', password='password')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    '''
    view sign up page
    '''
    def test_signup_view(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    '''
    test create account
    '''
    def test_valid_createuser(self):
        c = Client()
        form = {'username': 'account', 'password': 'account1234',
         'first_name': 'first', 'last_name': 'last', 'email': 'test@user.com', 'gender':"Male", 'birthday': "2003-05-28"}
        response = c.get(reverse('create_account'), form )
        self.assertTrue(response.status_code, 200)

    '''
    normal user can search room
    '''
    def test_normal_search_room(self):
        self.client.login(username='test', password='password')
        form = {'search': 'room'}
        response = self.client.get(reverse('search'), form)
        self.assertEqual(response.status_code, 200)
    
    '''
    test no text in search form
    '''
    def test_normal_search_room_notype(self):
        self.client.login(username='test', password='password')
        form = {'search': ''}
        response = self.client.get(reverse('search'), form)
        self.assertEqual(response.status_code, 302)

    '''
    test not fount room in search form
    '''
    def test_normal_search_room_not_found(self):
        self.client.login(username='test', password='password')
        form = {'search': 'notfound'}
        response = self.client.get(reverse('search'), form)
        self.assertEqual(response.status_code, 302)

    '''
    test search room that more than one
    '''
    def test_normal_search_room_multiply_found(self):
        self.client.login(username='test', password='password')
        form = {'search': 'empty'}
        response = self.client.get(reverse('search'), form)
        self.assertEqual(response.status_code, 200)

    '''
    normal user can sent help form
    '''
    def test_normal_send_help(self):
        self.client.login(username='user', password='password')
        form = {'help_send': 'this is my report'}
        response = self.client.get(reverse('help_send'), form)
        self.assertEqual(response.status_code, 302)

    

class LogInViewTest(TestCase):

    '''
    create user and create account
    create staff and his shop
    create admin user
    '''
    def setUp(self):
        self.client = Client()
        password = make_password('password')

        # create user
        user = User.objects.create(username='test', password=password)
        account = Account.objects.create(user=user)
        
        # create admin
        admin = User.objects.create_superuser(username="admin", password =password)
        
        # create staff and his shop
        staff = User.objects.create(username='staff', password=password)
        staff.is_staff = True
        staff.save()
        shop = Shop.objects.create(name="roomtest",staff=staff)
        shop.save()

    '''
    test login with valid user
    '''
    def test_valid_login(self):
        c = Client()
        form = {'username': 'test', 'password': 'password'}
        response = c.post(reverse('login'), form )
        self.assertTrue(response.status_code, 200)

    '''
    test login with alrady login
    '''
    def test_double_login(self):
        self.client.login(username='test', password='password')
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    '''
    test login with invalid user
    '''
    def test_invalid_login(self):
        c = Client()
        form = {'username': 'wronguser', 'password': 'fakepass'}
        response = c.post(reverse('login'), form )
        self.assertTrue(response.status_code, 200)

    '''
    test logout action by get
    '''
    def test_logout_get(self):
        self.client.login(username='test', password='password')
        response = self.client.get("/logout")
        self.assertEqual(response.status_code, 301)
        
    '''
    test logout action by post
    '''
    def test_logout_post(self):
        self.client.login(username='test', password='password')
        response = self.client.post("/logout")
        self.assertEqual(response.status_code, 301)

    '''
    test logout action no login
    '''
    def test_logout(self):
        c = Client()
        response = c.post(reverse("logout"))
        self.assertEqual(response.status_code, 302)

    '''
    test logout by request check
    '''
    def test_logout_request(self):
        self.client = Client()
        response = self.client.post(reverse("logout"))
        