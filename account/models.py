from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from chat.models import Room
# Create your models here.

class Account(models.Model):
	birthday = models.DateField(default=datetime.now)
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	bio = models.CharField(max_length=300, default="")
	image = models.ImageField(default='default.jpg', upload_to='profile_pics/',blank=True, null=True)
	chat = models.IntegerField(null=True)
	GenderType = [('M','Male'),
					('F', 'Female'),
					('L', 'LGBTQ+')]
	gender = models.CharField(blank=True, 
			choices=GenderType,
			max_length=10)

def __str__(self):
   	return self.title