from django.db import models
from django.urls import reverse

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

    def save(self,*ar):
        return super().save(force_insert, force_update, using, update_fields)
    def get_absolute_url(self):
        return reverse("productDetails", args=[self.id])

    def __str__(self):
        return self.name
