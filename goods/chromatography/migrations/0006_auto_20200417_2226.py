# Generated by Django 3.0.5 on 2020-04-17 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chromatography', '0005_auto_20200417_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gcsystem',
            name='product_code',
            field=models.CharField(default='GC-73155', max_length=8, unique=True),
        ),
    ]
