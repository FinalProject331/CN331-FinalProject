from django.db import models
from datetime import datetime

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=1000)
    id = models.AutoField(primary_key=True)
    seat_count = models.IntegerField(default=1)
    max_seat = models.IntegerField(default=2)
    GenderRequest = [('M', 'Male'),
                     ('F', 'Female'),
                     ('L', 'LGBTQ+'),
                     ('A', 'Any')]
    request_gender = models.CharField(blank=True,
                                      choices=GenderRequest,
                                      max_length=10)
    room_name = models.CharField
    start_time = models.DateTimeField(default=datetime.now, blank=True)
    dead_time = models.DateTimeField(default=datetime.today, blank=True)
    # hashtags = models.ManyToManyField(Tags)
    meal_time = models.DateTimeField(default=datetime.today, blank=True)
    status = models.BooleanField(default=True)
    # room_owner = models.ManyToManyField(Account, verbose_name="owner")

    def is_seat_available(self):
        return self.seat_count < self.max_seat


class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
