from django.db import models

# Create your models here.

class SiteSetting(models.Model):
    site_name = models.CharField(max_length=100,verbose_name="نام سایت")
    logo = models.ImageField
    
