# Generated by Django 3.0.5 on 2020-04-19 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spectrometry', '0008_auto_20200419_0304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasms',
            name='product_code',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='liquidms',
            name='product_code',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
