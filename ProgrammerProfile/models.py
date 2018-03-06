from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Person(models.Model):
    Name = models.CharField(max_length=100)
    age = models.IntegerField()
    Description = models.TextField()
    ProfilePic = models.FileField()

    def __str__(self):
        return self.Name
class Posts(models.Model):
    Name = models.CharField(max_length=1000000000000)        
    post = models.TextField()
    author = models.CharField(max_length=100)
    def __str__(self):
        return self.Name 