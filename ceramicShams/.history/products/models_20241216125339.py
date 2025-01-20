from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)  # ستون برای نام محصول
    description = models.TextField()         # ستون برای توضیحات
    price = models.IntegerField()  # ستون برای قیمت
# ستون برای آپلود عکس
    image = models.ImageField(
        upload_to='products/image/',  default='products/images/default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)  # زمان ایجاد
    updated_at = models.DateTimeField(auto_now=True)      # زمان به‌روزرسانی
    slug = models.SlugField(default="",null=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("productDetails", args=[self.id])

    def __str__(self):
        return self.name
