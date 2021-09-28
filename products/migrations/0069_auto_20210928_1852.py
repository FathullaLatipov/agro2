# Generated by Django 3.2.7 on 2021-09-28 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0068_remove_productmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='image44',
            field=models.FileField(blank=True, null=True, upload_to='products', verbose_name='image44'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='image77',
            field=models.FileField(blank=True, null=True, upload_to='products/textures', verbose_name='image77'),
        ),
    ]