# Generated by Django 3.0.5 on 2020-04-17 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chromatography', '0009_auto_20200417_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gcsystem',
            name='product_code',
            field=models.CharField(default='GC-7162230', editable=False, max_length=10, unique=True),
        ),
    ]
