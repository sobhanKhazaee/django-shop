# Generated by Django 5.1.4 on 2024-12-25 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0002_alter_banner_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='position',
            field=models.CharField(choices=[('home_top', 'صفحه اصلی - بالا'), ('home_middle', 'صفحه اصلی - وسط'), ('home_bottom', 'صفحه اصلی - پایین'), ('about_top', 'درباره ما - بالا'), ('about_bottom', 'درباره ما - پایین'), ('contact_top', 'تماس با ما - بالا'), ('contact_bottom', 'تماس با ما - پایین')], help_text='انتخاب موقعیت نمایش بنر', max_length=50, verbose_name='موقعیت بنر'),
        ),
    ]
