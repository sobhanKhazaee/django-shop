from django.db import models

# Create your models here.

class contact_us(models.Model):
    full_name = models.CharField(verbose_name='نام و نام خانوادگی')
    email = models.CharField(verbose_name='ایمیل')
    title = models.CharField(verbose_name='موضوع')
    massage = models.TextField(*ma)
    