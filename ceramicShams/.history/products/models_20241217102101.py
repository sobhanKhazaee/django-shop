from django.db import models
from django.urls import reverse
from slugify import slugify
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class category(models.Model):
    title = models

# مدل محصول
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    rate = models.IntegerField(null=True, validators=[
                               MinValueValidator(1), MaxValueValidator(5)], editable=False)
# ستون برای آپلود عکس
    image = models.ImageField(
        upload_to='products/image/',  default='products/images/default.jpg')
    slug = models.SlugField(null=False, blank=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  # زمان ایجاد
    updated_at = models.DateTimeField(auto_now=True)      # زمان به‌روزرسانی
   

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
