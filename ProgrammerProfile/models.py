from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Person(models.Model):
        Name = models.CharField(max_length=100)
        DOB = models.DateField()
        age = models.IntegerField()
        Description = models.TextField()
        Profile_Picture = models.FileField()

        def __str__(self):
                return self.Name

class Language(models.Model):
    user = models.ForeignKey(User)
    Language = models.CharField(max_length=100)

    def __str__(self):
        return self.Language+"-"+str(self.user)
