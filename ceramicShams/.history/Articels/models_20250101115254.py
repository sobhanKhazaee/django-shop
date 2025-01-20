from django.db import models

# Create your models here.

class AticelsList(models.Model):
    title = models.CharField(max_length=100,verbose_name="عنوان مقاله")
    image = models.ImageField(upload_to="articels/image",null=True,blank=True,verbose_name="عکس مقاله")
    summary = models.
    full_text = models.TextField(verbose_name="متن مقاله")
