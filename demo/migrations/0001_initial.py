# Generated by Django 4.0.5 on 2023-08-06 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=10, max_digits=20)),
                ('longitude', models.DecimalField(decimal_places=10, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='Drone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('weight', models.IntegerField(default=1)),
                ('distance', models.IntegerField(default=1)),
                ('status', models.CharField(default='off', max_length=25)),
                ('latitude', models.DecimalField(decimal_places=7, default='37.5566056', max_digits=20)),
                ('longitude', models.DecimalField(decimal_places=7, default='-122.0287363', max_digits=20)),
                ('battery', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DroneStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=200, unique=True)),
                ('brief', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DroneTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('status', models.CharField(default='OFF', max_length=200)),
                ('battery', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_address', models.CharField(default='36039 Pizzaro dr, Fremont, Ca, 94653', max_length=200)),
                ('departure_latitude', models.DecimalField(decimal_places=7, default='37.5566056', max_digits=20)),
                ('departure_longitude', models.DecimalField(decimal_places=7, default='-122.0287363', max_digits=20)),
                ('landing_address', models.CharField(default='35820 Fremont Blvd, Fremont, CA 94536', max_length=200)),
                ('landing_latitude', models.DecimalField(decimal_places=7, default='37.5605321', max_digits=20)),
                ('landing_longitude', models.DecimalField(decimal_places=7, default='-122.0180234', max_digits=20)),
                ('order_description', models.TextField()),
                ('weight', models.IntegerField(default=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(default='pending', max_length=250, unique=True)),
                ('status_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SystemHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('command', models.CharField(max_length=250, unique=True)),
                ('brief', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
