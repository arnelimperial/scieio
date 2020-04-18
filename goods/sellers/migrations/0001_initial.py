# Generated by Django 3.0.5 on 2020-04-17 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        ('manufacturers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True)),
                ('location', models.CharField(max_length=100)),
                ('website', models.URLField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True)),
                ('shipping_policy', models.CharField(default='', max_length=255)),
                ('return_policy', models.CharField(default='', max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('client_manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manufacturers', related_query_name='manufacturer', to='manufacturers.Manufacturer')),
                ('service_line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', related_query_name='service', to='categories.Category')),
            ],
            options={
                'ordering': ['id'],
                'unique_together': {('name', 'slug')},
            },
        ),
    ]
