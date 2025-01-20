from django.db import models

# Create your models here.

class SiteSetting(models.Model):
    name = models.CharField(max_length=length, ${blank=True, null=True})
    site_name = models.CharField(max_length=100,verbose_name="نام سایت")
    logo = models.ImageField(upload_to="site/image",verbose_name="لوگوی سایت")
    
