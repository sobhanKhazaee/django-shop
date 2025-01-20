from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)  # ستون برای نام محصول
    description = models.TextField()         # ستون برای توضیحات
    price = models.DecimalField(max_digits=10)  # ستون برای قیمت
    image = models.ImageField(upload_to='products/') 
    created_at = models.DateTimeField(auto_now_add=True)  # زمان ایجاد
    updated_at = models.DateTimeField(auto_now=True)      # زمان به‌روزرسانی

    def __str__(self):
        return self.name