from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CountryChoices(models.TextChoices):
    iran  = ('iran', 'ایران')
    usa = ('usa','امریکا')

class SubjectChoices(models.TextChoices):
    sport = ('1', 'ورزشی')
    social = ('2', 'شبکه اجتماعی')


    

class Post(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField('محتوا')
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('accounts.CustomUser', verbose_name='کاربر', on_delete=models.CASCADE)
    visible = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    subject = models.CharField(max_length=1, choices=SubjectChoices)
    
    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست'