from django.db import models

# Create your models here.

class AticelsList(models.Model):
    title = models.CharField(max_length=100,verbose_name="عنوان مقاله")
    image = models.ImageField(upload_to=, height_field=None, width_field=None, max_length=None)