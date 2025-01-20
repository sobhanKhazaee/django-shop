from django.db import models

class Banner(models.Model):
    POSITION_CHOICES = [
        ('home', 'صفحه اصلی'),
        ('about', 'درباره ما'),
        ('contact', 'تماس با ما'),
        # می‌توانید موقعیت‌های دیگر را اضافه کنید
    ]

    image = models.ImageField(verbose_name="تصویر بنر", upload_to='banners/')
    title = models.CharField(verbose_name="عنوان بنر", max_length=200, blank=True, null=True)
    description = models.TextField(verbose_name="توضیحات بنر", blank=True, null=True)
    link = models.URLField(verbose_name="لینک بنر", blank=True, null=True)
    position = models.CharField(verbose_name="موقعیت بنر", max_length=50, choices=POSITION_CHOICES, default='home')
    active = models.BooleanField(verbose_name="فعال/غیرفعال", default=True)
    created_at = models.DateTimeField(verbose_name="تاریخ ایجاد", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="تاریخ بروزرسانی", auto_now=True)

    def __str__(self):
        return f"{self.get_position_display()} - {self.title if self.title else 'بدون عنوان'}"

    class Meta:
        verbose_name = 'بنر'
        verbose_name_plural = 'بنرها'
        ordering = ['-created_at']
