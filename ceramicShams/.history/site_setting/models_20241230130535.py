from django.db import models

# Create your models here.


class SiteSetting(models.Model):
    domain = models.CharField(max_length=100, verbose_name="دامنه سایت")
    site_name = models.CharField(max_length=100, verbose_name="نام سایت")
    logo = models.ImageField(upload_to="site/image",
                             verbose_name="لوگوی سایت", null=True, blank=True)
    icon = models.ImageField(upload_to="site/image",
                             verbose_name="آیکون سایت", null=True, blank=True)
    about = models.TextField(
        verbose_name="توضیحات سایت"
    )
    phone_number = models.CharField(max_length=11, verbose_name="شماره تماس")
    email = models.EmailField(max_length=100, verbose_name="شماره تماس")

    class Meta:
        verbose_name = "تنظیمات سایت"
        verbose_name_plural = "تنظیمات"

    def __str__(self):
        return self.site_name


class LinkCategory(models.Model):
    linkCategory = models.CharField(
        max_length=100, verbose_name="دسته بندی لینک  های فوتر")

    class Meta:
        verbose_name = "دسته بندی لینک فوتر"
        verbose_name_plural = ""

    def __str__(self):
        return self.site_name
