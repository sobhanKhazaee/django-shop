from django.db import models
from django.urls import reverse
from slugify import slugify
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import CASCADE
fo
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="نام دسته")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = ' دسته بندی ها '

# برچسب ها


class ProductTags(models.Model):
    tag = models.CharField(max_length=100, verbose_name='برچسب')

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = 'برچسب'
        verbose_name_plural = 'برچسب ها'


class Brand(models.Model):
    brand_name = models.CharField(
        max_length=100,
        verbose_name='نام برند')

    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name = ' برند '
        verbose_name_plural = ' برند ها '
# مدل محصول


class Product(models.Model):
    # تعریف موقعیت ها در اسلایدر
    POSITION_SLIDER = [
        ('first', 'اسلایدر بالایی صفحه اول'),
        ('second', "اسلایدر پایین صفحه اول"),
        ('none', "در اسلایدر ها نباشد"),
    ]

    name = models.CharField(max_length=100, verbose_name='نام محصول')
    category = models.ForeignKey(
        Category, on_delete=CASCADE,
        related_name='products',
        verbose_name='دسته بندی محصول')

    description = models.TextField(verbose_name='توضیحات محصول')
    price = models.IntegerField(verbose_name='قیمت')
    rate = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(
            1), MaxValueValidator(5)],
        editable=False,
        verbose_name='امتیاز')
    product_tag = models.ManyToManyField(
        ProductTags,
        related_name='product_tags',
        null=True,
        blank=True
    )
    brand = models.ForeignKey(
        Brand, verbose_name="برند",
        on_delete=models.CASCADE,
        blank=True,
        null=True)

    # ستون برای آپلود عکس
    image = models.ImageField(
        upload_to='products/image/',
        null=True,
        verbose_name='عکس'
    )

    in_slider = models.CharField(
        max_length=100,
        choices=POSITION_SLIDER,
        verbose_name="موقعیت در اسلاید",
        null=True,
        blank=True
    )

    slug = models.CharField(max_length=50, verbose_name='اسلاگ', unique=True)
    is_active = models.BooleanField(
        default=False, verbose_name='فعال/غیر فعال')
    created_at = models.DateTimeField(auto_now_add=True)  # زمان ایجاد
    updated_at = models.DateTimeField(auto_now=True)      # زمان به‌روزرسانی

    # save slug with product name

    def save(self, *args, **kwargs):
        # i used allow_unicode=True to be able to use persian charcters while i make a slug
        if not self.slug:
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
