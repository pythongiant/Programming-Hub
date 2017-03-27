from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Person(models.Model):
        Name = models.ForeignKey(User)
        DOB = models.DateField()
        age = models.IntegerField()
        Description = models.TextField()
        Profile_Picture = models.ImageField(upload_to="/static")


