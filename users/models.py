from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    nickname = models.CharField(max_length=30, verbose_name='昵称')
    headshot = models.ImageField(upload_to='%Y/%m/%d',default='default.jpg', verbose_name='头像')

    class Meta(AbstractUser.Meta):
        pass