# Generated by Django 3.2.5 on 2021-08-03 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0028_remove_categoryhomemodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoryhomemodel',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.categorymodel', verbose_name='home_cat'),
        ),
    ]
