from django.db import models
from django.urls import reverse
from slugify import slugify

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100) 
    description = models.TextField()         
    price = models.IntegerField()  
    rate = models.IntegerField()
# ستون برای آپلود عکس
    image = models.ImageField(
        upload_to='products/image/',  default='products/images/default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)  # زمان ایجاد
    updated_at = models.DateTimeField(auto_now=True)      # زمان به‌روزرسانی
    slug = models.SlugField(default="", null=False)

    # save slug with product name
    def save(self, *args, **kwargs):
        # i used allow_unicode=True to be able to use persian charcters while i make a slug
        self.slug = slugify(self.name, allow_unicode=True)
        return super().save(*args, **kwargs)

    # this function return a dynamic url that i can use it in my templates
    def get_absolute_url(self):
        return reverse("productDetails", args=[self.slug])

    def __str__(self):
        return self.name
