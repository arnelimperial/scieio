# Generated by Django 3.0.5 on 2020-04-18 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spectrometry', '0005_auto_20200419_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasms',
            name='product_code',
            field=models.CharField(editable=False, max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='liquidms',
            name='product_code',
            field=models.CharField(editable=False, max_length=15, unique=True),
        ),
    ]
