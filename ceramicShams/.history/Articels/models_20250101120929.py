from django.db import models

# Create your models here.


class Aticel(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان مقاله")
    # add category
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


class ArticelCategories(models.model):
    title = models.CharField(
        max_length=100,
        verbose_name="عنوان دسته بندی",
        unique=True
    )
    url = models.URLField(max_length=100,verbose_name="عنوان در url",)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "دسته بندی مقالات"
        verbose_name_حم = "دسته بندی مقالات"
        
    
