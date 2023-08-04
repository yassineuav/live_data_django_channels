# Generated by Django 4.0.5 on 2023-08-03 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=200, unique=True)),
                ('description', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_address', models.CharField(max_length=200, unique=True)),
                ('to_address', models.CharField(max_length=200, unique=True)),
                ('from_location_lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('from_location_lon', models.DecimalField(decimal_places=6, max_digits=9)),
                ('to_location_lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('to_location_lon', models.DecimalField(decimal_places=6, max_digits=9)),
                ('describe', models.TextField()),
                ('weight', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='manager_order.status')),
            ],
        ),
    ]
