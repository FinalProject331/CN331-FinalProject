from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class Account(models.Model):
# 	user_id	= models.AutoField(primary_key=True)
# 	birthday = models.DateField()
# 	account = models.OneToOneField(User,on_delete=models.CASCADE)
# 	bio = models.CharField(max_length=300)
# 	profileimg = models.ImageField(default='default.jpg', upload_to='profile_pics',blank=True, null=True)
# 	GenderType = [('M','Male'),
# 					('F', 'Female'),
# 					('L', 'LGBTQ+')]
# 	gender = models.CharField(blank=True, 
# 			choices=GenderType,
# 			max_length=10)
	
# class Tags(models.Model):
# 	tags = models.CharField(max_length=300)

# class Room(models.Model):
# 	room_id = models.AutoField(primary_key=True)
# 	seat_count = models.IntegerField
# 	max_seat = models.IntegerField
# 	GenderRequest =[('M','Male'),
# 					('F', 'Female'),
# 					('L', 'LGBTQ+'),
# 					('A', 'Any')]
# 	request_gender = models.CharField(blank=True, 
# 			choices=GenderRequest,
# 			max_length=10)
# 	room_name = models.CharField
# 	start_time	= models.DateTimeField(default=datetime.now, blank=True)
# 	dead_time = models.DateTimeField()
# 	hashtags = models.ManyToManyField(Tags)
# 	meal_time = models.DateTimeField()
# 	status = models.BooleanField()
# 	room_owner = models.ManyToManyField(Account, verbose_name="owner")

# class Message(models.Model):
# 	value = models.CharField(max_length=300)
# 	date = models.DateTimeField(default=datetime.now, blank=True)
# 	user = models.CharField(max_length=30)
# 	room = models.CharField(max_length=64)

# class RestaurantChat(models.Model):
# 	staff = models.CharField(max_length=30)
# 	customer = models.CharField(max_length=30)
# 	restaurant_name = models.CharField(max_length=30)

# class Restaurant(models.Model):
# 	name = models.CharField(max_length=300)
# 	detail = models.CharField(max_length=300)
# 	profileimg = models.ImageField(default='default.jpg', upload_to='profile_pics',blank=True, null=True)
# 	location = models.CharField(max_length=300)
# 	chat_room = models.ManyToManyField(RestaurantChat, blank=True)

class Help(models.Model):
<<<<<<< HEAD
	report = models.CharField(max_length=300)
=======
	user = models.CharField(max_length=300)
	
>>>>>>> a3716ba150f3b146a81c52f0f349abc15051b890
	