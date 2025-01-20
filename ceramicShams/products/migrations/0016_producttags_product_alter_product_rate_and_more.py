# Generated by Django 5.1.4 on 2024-12-17 21:10

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_alter_producttags_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttags',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_tags', to='products.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='rate',
            field=models.IntegerField(blank=True, editable=False, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='امتیاز'),
        ),
        migrations.AlterField(
            model_name='producttags',
            name='tag',
            field=models.CharField(max_length=100, verbose_name='برچسب'),
        ),
    ]
