from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=128,unique=True)#用于登录的用户名，必须唯一
    password = models.CharField(max_length=256)#密码
    