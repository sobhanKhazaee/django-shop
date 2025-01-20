from django.db import models
from django.db.models import CASCADE

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
    phone_number = models.CharField(max_length=11, verbose_name="شماره تماس",null=True)
    email = models.EmailField(max_length=100, verbose_name="ایمیل",null=True)

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
        verbose_name_plural = "دسته بندی های لینک های فوتر"

    def __str__(self):
        return self.linkCategory


class FooterLinks(models.Model):
    cat = models.ForeignKey(LinkCategory, on_delete=CASCADE,verbose_name="دسته بندی لینک")
    link = models.CharField(max_length=100,verbose_name="لینک")
    link_title = models.CharField(max_length=50,verbose_name="عنوان لینک")

    class Meta:
        verbose_name = "لینک  فوتر"
        verbose_name_plural = "لینک های فوتر"

    def __str__(self):
        return self.link_title

class SocialMedia(models.Model):
    link = models.CharField(max_length=100,verbose_name="لینک")
    icon = models.CharField(max_length=200,ve)
        