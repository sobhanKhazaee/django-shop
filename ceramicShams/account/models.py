from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    # mobile = models.CharField(max_length=11, verbose_name="شماره موبایل")
    email_active_code = models.CharField(
        max_length=100, verbose_name="کد فعالسازی ایمیل")
    phone_nember = models.CharField(max_length=11, verbose_name="شماره تلفن")
    address = models.TextField(verbose_name="آدرس") 
    postal_code = models.CharField(max_length=10, verbose_name="کد پستی")
    image_profile = models.ImageField(upload_to="users/image", null=True, blank=True, verbose_name="عکس پروفایل")

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.username
