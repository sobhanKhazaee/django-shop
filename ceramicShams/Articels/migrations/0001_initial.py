# Generated by Django 5.1.4 on 2025-01-01 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticelCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='عنوان دسته بندی')),
                ('url', models.URLField(help_text='عنوان درurl باید کارکاتر های انگلیسی باشد', max_length=100, verbose_name='عنوان در url')),
            ],
            options={
                'verbose_name': 'دسته بندی مقالات',
                'verbose_name_plural': 'دسته بندی های مقالات',
            },
        ),
        migrations.CreateModel(
            name='Aticel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان مقاله')),
                ('image', models.ImageField(blank=True, null=True, upload_to='articels/image', verbose_name='عکس مقاله')),
                ('summary', models.TextField(max_length=500, verbose_name='خلاصه مقاله')),
                ('full_text', models.TextField(verbose_name='متن مقاله')),
                ('author', models.CharField(max_length=100, verbose_name='نویسنده')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال/غیرفعال')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='آخرین بروز رسانی')),
            ],
        ),
    ]
