# Generated by Django 3.2.5 on 2021-07-19 11:20

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_alter_productmodel_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorymodel',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='brandmodel',
            name='title_en',
            field=models.CharField(max_length=30, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='brandmodel',
            name='title_ru',
            field=models.CharField(max_length=30, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='brandmodel',
            name='title_uz',
            field=models.CharField(max_length=30, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='title_en',
            field=models.CharField(max_length=30, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='title_ru',
            field=models.CharField(max_length=30, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='title_uz',
            field=models.CharField(max_length=30, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='long_description_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='long_description'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='long_description_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='long_description'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='long_description_uz',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='long_description'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='short_description_en',
            field=models.TextField(null=True, verbose_name='short_description'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='short_description_ru',
            field=models.TextField(null=True, verbose_name='short_description'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='short_description_uz',
            field=models.TextField(null=True, verbose_name='short_description'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='title_en',
            field=models.CharField(max_length=90, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='title_ru',
            field=models.CharField(max_length=90, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='title_uz',
            field=models.CharField(max_length=90, null=True, verbose_name='title'),
        ),
    ]