from django.db import models

# Create your models here.


class SiteSetting(models.Model):
    domain = models.CharField(max_length=100, verbose_name="دامنه سایت")
    site_name = models.CharField(max_length=100, verbose_name="نام سایت")
    logo = models.ImageField(upload_to="site/image", verbose_name="لوگوی سایت")
    logo = models.ImageField(upload_to="site/image", verbose_name="لوگوی سایت",null=True,blank=True)
    about = models.TextField(
        verbose_name="توضیحات سایت",
        help_text="این متن در فوتر(پاورقی)  سایت استفاده میشود"
    )
    سخزهشم
    
    class Meta:
        verbose_name = "تنظیمات سایت"
        verbose_plural_name = "تنظیمات"
    
    def __str__(self):
        return self.site_name
    
