from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)  # ستون برای نام محصول
    description = models.TextField()         # ستون برای توضیحات
    price = models.DecimalField(max_digits=10, decimal_places=2)  # ستون برای قیمت
    created_at = models.DateTimeField(auto_now_add=True)  # زمان ایجاد
    updated_at = models.DateTimeField(auto_now=True)      # زمان به‌روزرسانی

    def __str__(self):
        return self.name