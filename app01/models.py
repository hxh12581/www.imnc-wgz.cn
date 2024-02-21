from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=25)


class Group(models.Model):
    user_id = models.CharField(max_length=25)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    group_id = models.CharField(max_length=25)
    count = models.IntegerField(default=0)
    userFace = models.TextField()
