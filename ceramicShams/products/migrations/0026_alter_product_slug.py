# Generated by Django 5.1.4 on 2024-12-31 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.CharField(max_length=50, unique=True, verbose_name='اسلاگ'),
        ),
    ]
