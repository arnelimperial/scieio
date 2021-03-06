# Generated by Django 3.0.5 on 2020-04-17 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chromatography', '0003_gcsystem'),
        ('sellers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gcsystem',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sellers.Seller'),
        ),
        migrations.AlterUniqueTogether(
            name='gcsystem',
            unique_together={('name', 'slug')},
        ),
    ]
