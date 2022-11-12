from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

class Help(models.Model):
	user = models.CharField(max_length=300)
	
	