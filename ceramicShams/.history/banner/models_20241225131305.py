from django.db import models


class Banner(models.Model):

    POSITION_CHOICES = [
        ('home_top', 'صفحه اصلی - بالا'),
        ('home_middle', 'صفحه اصلی - وسط'),
        ('home_bottom', 'صفحه اصلی - پایین'),
        ('about_top', 'درباره ما - بالا'),
        ('about_bottom', 'درباره ما - پایین'),
        ('contact_top', 'تماس با ما - بالا'),
        ('contact_bottom', 'تماس با ما - پایین'),
        # موقعیت‌های دلخواه دیگر
    ]

    image = models.ImageField(
        verbose_name="تصویر بنر",
        upload_to='banners/',
        help_text="لطفاً تصویر با کیفیت مناسب را بارگذاری کنید."
    )
    title = models.CharField(
        verbose_name="عنوان بنر",
        max_length=200,
        blank=True,
        null=True,
        help_text="عنوان بنر (اختیاری)"
    )
    description = models.TextField(
        verbose_name="توضیحات بنر",
        blank=True,
        null=True,
        help_text="توضیحات بنر (اختیاری)"
    )
    link = models.URLField(
        verbose_name="لینک بنر",
        blank=True,
        null=True,
        help_text="لینک مقصد بنر (اختیاری)"
    )
    position = models.CharField(
        verbose_name="موقعیت بنر",
        max_length=50,
        choices=POSITION_CHOICES,
        help_text="انتخاب موقعیت نمایش بنر"
    )
    active = models.BooleanField(
        verbose_name="فعال/غیرفعال",
        default=True,
        help_text="فعال کردن یا غیرفعال کردن بنر"
    )
    created_at = models.DateTimeField(
        verbose_name="تاریخ ایجاد",
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="تاریخ بروزرسانی",
        auto_now=True
    )

    def __str__(self):
        return f"{self.get_position_display()} - {self.title if self.title else 'بدون عنوان'}"

    class Meta:
        verbose_name = 'بنر'
        verbose_name_plural = 'بنرها'
        ordering = ['-created_at']
