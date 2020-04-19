# Generated by Django 3.0.5 on 2020-04-19 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manufacturers', '0001_initial'),
        ('sellers', '0004_auto_20200418_0002'),
        ('analytical_instruments', '0001_initial'),
        ('conditions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElementalAnalyzer',
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
                ('instrumentation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analytical_instruments.Instrumentation')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manufacturers.Manufacturer')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sellers.Seller')),
            ],
            options={
                'ordering': ['id'],
                'unique_together': {('name', 'slug')},
            },
        ),
    ]
