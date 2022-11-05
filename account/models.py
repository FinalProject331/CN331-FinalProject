from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Account(models.Model):
	birthday = models.DateField(default=datetime.now)
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	bio = models.CharField(max_length=300, default="")
	profileimg = models.ImageField(default='default.png', upload_to='profile_pics',blank=True, null=True)
	GenderType = [('M','Male'),
					('F', 'Female'),
					('L', 'LGBTQ+')]
	gender = models.CharField(blank=True, 
			choices=GenderType,
			max_length=10)
	