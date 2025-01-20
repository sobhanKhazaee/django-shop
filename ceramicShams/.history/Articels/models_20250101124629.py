from django.db import models
from unidecode import unidecode
from django.db.models import CASCADE

# Create your models here.


class ArticelCategories(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="عنوان دسته بندی",
        unique=True
    )
    url = models.URLField(
        max_length=100,
        verbose_name="عنوان در url",
        help_text="عنوان درurl باید کارکاتر های انگلیسی باشد",
        null=True, blank=True
    )

    def save(self, *args, **kwargs):
        if self.url is None:
            self.url = unidecode(self.title)
        return super().save(self, *args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی مقالات"
        verbose_name_plural = "دسته بندی های مقالات"


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
