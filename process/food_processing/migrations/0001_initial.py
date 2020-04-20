# Generated by Django 3.0.5 on 2020-04-20 03:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('conditions', '0001_initial'),
        ('manufacturers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodProcessing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True)),
                ('description', models.TextField()),
                ('product_code', models.CharField(editable=False, max_length=15, unique=True)),
                ('model', models.CharField(max_length=255, unique=True)),
                ('warranty', models.BooleanField(default=True)),
                ('image', models.URLField()),
                ('availability', models.BooleanField(default=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('condition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conditions.Condition')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manufacturers.Manufacturer')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
