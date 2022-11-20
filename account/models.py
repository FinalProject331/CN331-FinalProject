from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Account(models.Model):
	birthday = models.DateField(default=datetime.now)
	user = models.OneToOneField(User,on_delete=models.CASCADE ,related_name='profile') 
	bio = models.CharField(max_length=300, default="")
	image = models.ImageField(default='default.png', upload_to='profile_pics/',blank=True, null=True)
	chat = models.IntegerField(default=0)
	GenderType = [('M','Male'),
					('F', 'Female'),
					('L', 'LGBTQ+')]
	gender = models.CharField(blank=True, 
			choices=GenderType,
			max_length=10)
	age = models.CharField(max_length=10, default=0)

	def save(self,*args, **kwargs):
		super().save(*args, ** kwargs)
		img = Image.open(self.image.path)
		if img.height > 300 or img.width > 300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)

