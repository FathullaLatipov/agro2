# Generated by Django 3.2.5 on 2021-07-07 20:47

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_productmodel_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='long_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]