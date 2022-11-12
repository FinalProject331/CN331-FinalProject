from django.db import models
from location_field.models.plain import PlainLocationField
from django.contrib.auth.models import User

# Create your models here.

class ShopChat(models.Model):
	staff = models.CharField(max_length=30)
	customer = models.CharField(max_length=30)
	restaurant_name = models.CharField(max_length=30)

class Shop(models.Model):
	name = models.CharField(max_length=300)
	detail = models.CharField(max_length=300)
	shopimg = models.ImageField(default='default.jpg', upload_to='profile_pics',blank=True, null=True)
	location = models.CharField(max_length=300)
	chat_room = models.ManyToManyField(ShopChat, blank=True)
	location = PlainLocationField(based_fields=['name'], zoom=7)
	staff = models.OneToOneField(User,on_delete=models.CASCADE ,related_name='staff',null=True) 

class AddShop(models.Model):
	user = models.CharField(max_length=300)