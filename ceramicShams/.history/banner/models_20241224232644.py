from django.db import models

# Create your models here.


class Banner1(models.Model):
    banner_ = models.ImageField(verbose_name="1 بنر ")

    def __str__(self):
        return self.image

    class Meta:
        verbose_name = ' بنر  '
        verbose_name_plural = ' بنرها '
