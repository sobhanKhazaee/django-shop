from django.db import models
from unidecode import unidecode
from django.db.models import CASCADE
# from account.models import User
from 

# Create your models here.

""" 
    دسته بندی مقالات
 """


class ArticelCategories(models.Model):

    title = models.CharField(
        max_length=100,
        verbose_name="عنوان دسته بندی",
        unique=True
    )
    url = models.CharField(
        max_length=100,
        verbose_name="عنوان در url",
        help_text="عنوان درurl باید کارکاتر های انگلیسی باشد",
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        if not self.url:
            # استفاده از unidecode برای تبدیل به کاراکترهای انگلیسی و حذف `/`
            self.url = unidecode(f"{self.title}").replace(
                " ", "-").replace("/", "-")
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی مقالات"
        verbose_name_plural = "دسته بندی های مقالات"


""" 
مقالات
"""


class Aticel(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان مقاله")
    category = models.ForeignKey(
        ArticelCategories,
        verbose_name=("دسته بندی مقاله"),
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to="articels/image", null=True, blank=True, verbose_name="عکس مقاله")
    summary = models.TextField(max_length=500, verbose_name="خلاصه مقاله")
    full_text = models.TextField(verbose_name="متن مقاله")
    author = models.CharField(max_length=100, verbose_name="نویسنده")
    is_active = models.BooleanField(default=False, verbose_name="فعال/غیرفعال")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="آخرین بروز رسانی")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = " مقاله "
        verbose_name_plural = " مقالات"


""" 
نظرات مقالات
"""


class ArticelComments(models.Model):
    # اسن کامنت متعلق به کدام مقاله است
    article = models.ForeignKey(
        Aticel, on_delete=CASCADE, verbose_name="مقاله")
    # این کامنت اصلی است یا پاسخ به کامنت دیگر
    parent = models.ForeignKey(
        'ArticelComments',
        on_delete=CASCADE,
        null=True,
        blank=True,
        verbose_name="پاسخ به"
    )
    # این کامنت متعلق به کدام کاربر است
    user = models.ForeignKey(User,on_delete=CASCADE,verbose_name="کاربر")
    comment = models.TextField(max_length=500,verbose_name="نظر")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "نظر مقاله"
        verbose_name_plural = " نظرات مقاله "

    def __str__(self):
        return self.article