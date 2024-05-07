# api/models.py

from django.db import models

class User(models.Model):
    UserNO = models.CharField(max_length=50)
    UserName = models.CharField(max_length=50)
    Bless = models.CharField(max_length=50)

    def __str__(self):
        return self.UserName
