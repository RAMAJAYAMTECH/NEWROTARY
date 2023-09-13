from django.db import models
from django.db.models.base import ModelStateFieldsCacheDescriptor

# Create your models here.

class login(models.Model):
    user_name=models.CharField('user_name',max_length=100)
    password=models.CharField('password',max_length=100)
    email=models.EmailField('email')

    def __str__(self):
        return self.user_name

class user_page(models.Model):
    no_of_works=models.IntegerField()
    duration=models.TimeField()
    client_name=models.CharField(max_length=100)
    describtion=models.CharField(max_length=600)

    def __str__(self):
        return self.client_name

class report(models.Model):
    time=models.TimeField()
    client_name=models.CharField(max_length=100)
    describtion=models.CharField(max_length=600)

    def __str__(self):
        return self.client_name