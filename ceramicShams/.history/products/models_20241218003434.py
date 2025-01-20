from django.db import models
from django.urls import reverse
from slugify import slugify
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import CASCADE

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="نام دسته")
    cat_url = models.CharField(max_length=100, verbose_name="url دسته بندی")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = ' دسته بندی ها '


class ProductTags(models.Model):
    tag = models.CharField(max_length=100, verbose_name='برچسب')
      product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_tags')
    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = 'برچسب'
        verbose_name_plural = 'برچسب ها'


# مدل محصول


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام محصول')
    category = models.ForeignKey(
        Category, on_delete=CASCADE,
        related_name='products',
        verbose_name='دسته بندی محصول')
    description = models.TextField(verbose_name='توضیحات محصول')
    price = models.IntegerField(verbose_name='قیمت')
    rate = models.IntegerField(
        blank=True,
        validators=[MinValueValidator(
            1), MaxValueValidator(5)],
        editable=False,
        verbose_name='امتیاز')
    tags = models.ManyToManyField(
        ProductTags,
        verbose_name='برچسب ها',
        null=True)
    # ستون برای آپلود عکس
    image = models.ImageField(
        upload_to='products/image/', null=True, verbose_name='عکس')
    slug = models.SlugField(null=False, blank=True, verbose_name='اسلاگ')
    is_active = models.BooleanField(
        default=False, verbose_name='فعال/غیر فعال')
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

    class Meta:
        verbose_name = ' محصول '
        verbose_name_plural = ' محصولات '
