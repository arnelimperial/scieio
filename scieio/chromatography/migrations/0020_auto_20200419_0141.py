# Generated by Django 3.0.5 on 2020-04-18 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chromatography', '0019_auto_20200419_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gcsystem',
            name='product_code',
            field=models.CharField(default='GC-5007887', editable=False, max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='lc',
            name='product_code',
            field=models.CharField(default='LC-4907853', editable=False, max_length=10, unique=True),
        ),
    ]