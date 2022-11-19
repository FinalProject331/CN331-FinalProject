from django.test import TestCase, Client
from .models import Shop, ShopChat
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

        # create staff
        staff = User.objects.create(username='staff', password=password)
        staff.is_staff = True
        staff.save()

        # create staff shop
        shop = Shop.objects.create(name="roomtest",staff=staff)
        shop.save()

        # create user
        normal_user = User.objects.create(username="user",password=password)
        normal_account = Account.objects.create(user=normal_user)
        testuser = User.objects.create(username = "test",password=password)
        Account.objects.create(user=testuser)

        # create admin
        User.objects.create(username="admin", password=password)
        admin = User.objects.get(username="admin")
        admin.is_superuser = True
        admin.save()

        # create staff chat room with normal_user
        chat = ShopChat.objects.create(name = "chat", 
        staff = staff.username,customer = normal_user.username,
        restaurant_name = "roomtest", customer_id = normal_user)


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
    test upload yorself a shop image success
    '''
    def test_upload_shop_image_success(self):
        self.client.login(username='staff', password='password')
        form = {'image':"default.jpg"}

        response = self.client.post(reverse('shopupload'), form)
        self.assertEqual(response.status_code, 302)

    '''
    test upload yorself a shop image use method get
    '''
    def test_upload_shop_image_method_get(self):
        self.client.login(username='staff', password='password')
        form = {'image':"default.jpg"}

        response = self.client.get(reverse('shopupload'))
        self.assertEqual(response.status_code, 200)
    
    '''
    test upload yorself a shop image invalid_form
    '''
    def test_upload_shop_image_invalid_form(self):
        self.client.login(username='staff', password='password')
        form = {'image':"invalid form"}

        response = self.client.post(reverse('shopupload'), form)
        self.assertEqual(response.status_code, 302)

    '''
    test upload yorself a shop image not post
    '''
    def test_upload_shop_image_not_post(self):
        self.client.login(username='staff', password='password')

        response = self.client.post(reverse('shopupload'))
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
    login normal user
    view shop list
    '''
    def test_user_view_shoplist(self):
        self.client.login(username='user', password='password')
        response = self.client.get(reverse('shoplist'))
        self.assertEqual(response.status_code, 200)

    '''
    login admin user
    view shop list
    '''
    def test_user_view_shoplist_admin(self):
        self.client.login(username='admin', password='password')
        response = self.client.post(reverse('shoplist'))
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

        '''
    normal user can search shop
    '''
    def test_normal_search(self):
        self.client.login(username='user', password='password')
        form = {'search_shop': 'this is search'}
        response = self.client.get(reverse('search_shop'), form)
        self.assertEqual(response.status_code, 302)
        '''
    normal user can search shop by no type form
    '''
    def test_normal_searchp_notype(self):
        self.client.login(username='user', password='password')
        form = {'search_shop': ''}
        response = self.client.get(reverse('search_shop'), form)
        self.assertEqual(response.status_code, 302)
        '''
    normal user can search shop by valid
    '''
    def test_normal_search_valid(self):
        self.client.login(username='user', password='password')
        form = {'search_shop': 'room'}
        response = self.client.get(reverse('search_shop'), form)
        self.assertEqual(response.status_code, 200)

    '''
    user view shop detail
    '''
    def test_user_view_shop_detail(self):
        self.client.login(username='user', password='password')
        room = Shop.objects.get(name="roomtest")

        response = self.client.get(reverse('viewshop' , args=[room.id]))
        self.assertEqual(response.status_code, 200)

    '''
    user view shop detail admin
    '''
    def test_user_view_shop_detail_admin(self):
        self.client.login(username='admin', password='password')
        room = Shop.objects.get(name="roomtest")

        response = self.client.get(reverse('viewshop' , args=[room.id]))
        self.assertEqual(response.status_code, 200)

    """
    action chat with staff by url directly valid
    """
    def test_join_chat_staff_directly_valid(self):
        self.client.login(username='staff', password='password')
        user = User.objects.get(username="user")
        chat = ShopChat.objects.get(staff = "staff")
        response = self.client.get('/shop/'+str(chat.name)+'/?username='+user.username, args=[str(chat.name)])
        self.assertEqual(response.status_code, 200)

    """
    action chat with user by url directly valid
    """
    def test_join_chat_user_directly_valid(self):
        self.client.login(username='user', password='password')
        user = User.objects.get(username="user")
        chat = ShopChat.objects.get(staff = "staff")
        response = self.client.get('/shop/'+str(chat.name)+'/?username='+user.username, args=[str(chat.name)])
        self.assertEqual(response.status_code, 200)

    '''
    test check view case there is room already
    '''
    def test_shop_check_view_exist_true(self):
        self.client.login(username='user', password='password')
        shop = Shop.objects.get(name="roomtest")
        response = self.client.get(reverse('shopcheckview' , args=[shop.name]))
        self.assertEqual(response.status_code, 302)

    '''
    test check view case there is no room exist()
    '''
    def test_shop_check_view_exist_false(self):
        self.client.login(username='test', password='password')
        shop = Shop.objects.get(name="roomtest")
        response = self.client.get(reverse('shopcheckview' , args=[shop.name]))
        self.assertEqual(response.status_code, 302)

    