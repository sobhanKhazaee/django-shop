from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)  # ستون برای نام محصول
    description = models.TextField()         # ستون برای توضیحات
    price = models.IntegerField()  # ستون برای قیمت
    image = models.ImageField(upload_to='products/image/' ,  default='products/images/default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)  # زمان ایجاد
    updated_at = models.DateTimeField(auto_now=True)      # زمان به‌روزرسانی



    def __str__(self):
        return self.name