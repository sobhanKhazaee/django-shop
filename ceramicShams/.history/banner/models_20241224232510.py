from django.db import models

# Create your models here.


class Banner1(models.Model):
    banner_1 = models.ImageField(verbose_name=" بنر ")

    def __str__(self):
        return self.image

    class Meta:
        verbose_name = ' بنر ها '
        verbose_name_plural = ''
