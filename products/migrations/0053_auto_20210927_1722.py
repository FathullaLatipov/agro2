# Generated by Django 3.2.7 on 2021-09-27 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0052_auto_20210927_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='image77',
            field=models.FileField(null=True, upload_to='products', verbose_name='image77'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='image88',
            field=models.FileField(null=True, upload_to='products', verbose_name='image88'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='image99',
            field=models.FileField(null=True, upload_to='products', verbose_name='image99'),
        ),
    ]