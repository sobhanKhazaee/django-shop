# Generated by Django 5.1.4 on 2025-01-05 07:59

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Articels', '0007_alter_aticel_full_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aticel',
            name='full_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='متن مقاله'),
        ),
    ]
