# Generated by Django 5.1.4 on 2024-12-17 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_producttags_product_alter_product_rate_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producttags',
            old_name='product',
            new_name='product_tag',
        ),
    ]
