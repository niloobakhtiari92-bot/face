from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    profile_picture = models.ImageField(upload_to='profile_pictures', default='avatar.png')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربر'

    def __str__(self):
        return self.username

    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name = 'کاربر'