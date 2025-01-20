from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    mobile = models.CharField(max_length=11, verbose_name="شماره موبایل")
    email_active_code = models.CharField(
        max_length=100, verbose_name="کد فعالسازی ایمیل")

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
        
    def    
