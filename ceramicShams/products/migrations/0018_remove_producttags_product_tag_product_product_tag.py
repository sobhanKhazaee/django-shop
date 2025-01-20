# Generated by Django 5.1.4 on 2024-12-17 21:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_rename_product_producttags_product_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producttags',
            name='product_tag',
        ),
        migrations.AddField(
            model_name='product',
            name='product_tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_tags', to='products.producttags'),
        ),
    ]
