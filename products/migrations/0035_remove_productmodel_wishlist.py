# Generated by Django 3.2.6 on 2021-08-17 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0034_alter_productmodel_wishlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='wishlist',
        ),
    ]