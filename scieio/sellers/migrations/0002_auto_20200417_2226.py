# Generated by Django 3.0.5 on 2020-04-17 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturers', '0001_initial'),
        ('sellers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='client_manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_manufacturers', related_query_name='client_manufacturer', to='manufacturers.Manufacturer'),
        ),
    ]
