from django.db import models

# Create your models here.

class Aticel(models.Model):
    title = models.CharField(max_length=100,verbose_name="عنوان مقاله")
    # addd
    image = models.ImageField(upload_to="articels/image",null=True,blank=True,verbose_name="عکس مقاله")
    summary = models.TextField(max_length=500,verbose_name="خلاصه مقاله" )
    full_text = models.TextField(verbose_name="متن مقاله")
    author = models.CharField(max_length=100,verbose_name="نویسنده")
    is_active = models.BooleanField(default=False,verbose_name="فعال/غیرفعال")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="آخرین بروز رسانی")

    