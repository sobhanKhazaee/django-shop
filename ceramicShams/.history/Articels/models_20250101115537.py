from django.db import models

# Create your models here.

class Aticel(models.Model):
    title = models.CharField(max_length=100,verbose_name="عنوان مقاله")
    image = models.ImageField(upload_to="articels/image",null=True,blank=True,verbose_name="عکس مقاله")
    summary = models.TextField(max_length=500,verbose_name="خلاصه مقاله" )
    full_text = models.TextField(verbose_name="متن مقاله")
    author = models.CharField(max_length=100,verbose_name="نویسنده")
    created_at = mo
