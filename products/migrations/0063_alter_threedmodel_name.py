# Generated by Django 3.2.7 on 2021-09-28 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0062_alter_threedmodel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='threedmodel',
            name='name',
            field=models.CharField(max_length=29, null=True),
        ),
    ]
