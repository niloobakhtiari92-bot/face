from django.db import models

# Create your models here.
class CountryCoices(models.TextChoices):
    iran = ('iran', 'ایران')
    usa = ('usa', 'امریکا')

class SubjectChoices(models.TextChoices):
    sport = ('1','ورزشی')
    social = ('2', 'شبکه اجتماعی')

class User(models.Model):
    username = models.CharField(max_length=60 , verbose_name = 'نام کاربری')
    passord = models.CharField('گذرواژه',max_length=32)
    birthdate = models.DateField('تاریخ تولد')
    email = models.EmailField('ایمیل')
    phone = models.CharField('تلفن')
    profile_pic = models.ImageField('عکس پروفایل',upload_to='profile_picutres')
    country = models.CharField('کشور',max_length=20,choices= CountryCoices, default= CountryCoices.iran)
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.username}'
    
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural ='کاربر'
   
class Post(models.Model):
    title = models.CharField('عنوان',max_length=60)
    content = models.TextField('محتوا')
    create_add= models.DateField('تاریخ')
    user = models.ForeignKey(to=User ,verbose_name = 'کاربر', on_delete=models.CASCADE)
    visible = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    subject = models.CharField('عنوان',max_length=1 , choices=SubjectChoices)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست'
