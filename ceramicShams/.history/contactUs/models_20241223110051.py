from django.db import models

# Create your models here.


class contact_us(models.Model):
    full_name = models.CharField(
        max_length=100,
        verbose_name='نام و نام خانوادگی'
    )
    email = models.CharField(max_length=100, verbose_name='ایمیل')
    title = models.CharField(max_length=100, verbose_name='موضوع')
    massage = models.TextField(max_length=600, verbose_name="پیام")
    created_at = models.DateTimeField(verbose_name="تاریخ", auto_now_add=True)

    class Meta:
        verbose_name = ' تیکت '
        verbose_name_plural = ' تیکت ها '
