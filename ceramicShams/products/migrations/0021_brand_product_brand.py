# Generated by Django 5.1.4 on 2024-12-18 11:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_remove_producttags_product_tag_product_product_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=100, verbose_name='نام برند')),
            ],
            options={
                'verbose_name': ' برند ',
                'verbose_name_plural': ' برند ها ',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.brand', verbose_name='برند'),
        ),
    ]
