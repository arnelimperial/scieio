# Generated by Django 3.0.5 on 2020-04-17 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chromatography', '0008_auto_20200417_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gcsystem',
            name='model',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='gcsystem',
            name='product_code',
            field=models.CharField(default='GC-5962434', editable=False, max_length=10, unique=True),
        ),
    ]
