# Generated by Django 3.0.5 on 2020-04-19 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spectrometry', '0010_auto_20200419_0412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liquidms',
            name='product_code',
            field=models.CharField(editable=False, max_length=15, unique=True),
        ),
    ]