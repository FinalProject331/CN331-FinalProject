from django.db import models
from datetime import datetime
from location_field.models.plain import PlainLocationField
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


class ShopChat(models.Model):
    name = models.CharField(max_length=300, default="")
    staff = models.CharField(max_length=30)
    customer = models.CharField(max_length=30)
    restaurant_name = models.CharField(max_length=30)
    customer_id = models.OneToOneField(User, on_delete = models.CASCADE, null = True)


class Shop(models.Model):
    name = models.CharField(max_length=300)
    # id = models.AutoField(primary_key=True)
    detail = models.CharField(max_length=300)
    shopimg = models.ImageField(
        default='default.png', upload_to='profile_pics/', blank=True, null=True)
    location = models.CharField(max_length=300)
    # chat_room = models.ManyToManyField(ShopChat, blank=True)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    staff = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='staff', null=True)
    def save(self, *args, **kwargs):
        super().save(*args, ** kwargs)
        img = Image.open(self.shopimg.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.shopimg.path)


class AddShop(models.Model):
    shop_name = models.CharField(max_length=300, default="", blank=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user', null=True)


class ShopMessage(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
