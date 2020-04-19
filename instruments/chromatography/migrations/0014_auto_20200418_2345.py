# Generated by Django 3.0.5 on 2020-04-18 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chromatography', '0013_auto_20200418_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gcsystem',
            name='product_code',
            field=models.CharField(default='GC-744223', editable=False, max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='lc',
            name='product_code',
            field=models.CharField(default='LC-1355920', editable=False, max_length=10, unique=True),
        ),
    ]
