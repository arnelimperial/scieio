# Generated by Django 3.0.5 on 2020-04-16 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturer',
            name='website',
            field=models.URLField(max_length=100, unique=True),
        ),
    ]
