# Generated by Django 5.1.4 on 2025-01-01 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0028_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, help_text='پیشنهاد میشود این فیلد را خالی بگذارید', null=True, unique=True, verbose_name='اسلاگ'),
        ),
    ]
