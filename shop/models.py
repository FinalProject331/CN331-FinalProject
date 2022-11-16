from django.db import models
from datetime import datetime
from location_field.models.plain import PlainLocationField
from django.contrib.auth.models import User

# Create your models here.


class ShopChat(models.Model):
    name = models.CharField(max_length=300, default="")
    staff = models.CharField(max_length=30)
    customer = models.CharField(max_length=30)
    restaurant_name = models.CharField(max_length=30)


class Shop(models.Model):
    name = models.CharField(max_length=300)
    id = models.AutoField(primary_key=True)
    detail = models.CharField(max_length=300)
    shopimg = models.ImageField(
        default='defaultStaff.png', upload_to='profile_pics/', blank=True, null=True)
    location = models.CharField(max_length=300)
    chat_room = models.ManyToManyField(ShopChat, blank=True)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    staff = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='staff', null=True)



class AddShop(models.Model):
    user = models.CharField(max_length=300)

class ShopMessage(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)