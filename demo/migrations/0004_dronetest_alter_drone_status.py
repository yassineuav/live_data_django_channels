# Generated by Django 4.0.5 on 2023-06-13 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_drone_distance_drone_weight'),
    ]

    operations = [
        migrations.CreateModel(
            name='DroneTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('status', models.IntegerField(choices=[(0, 'OFF'), (1, 'ON'), (2, 'Starting'), (3, 'Pending'), (4, 'shutting off')], default=0)),
                ('battery', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='drone',
            name='status',
            field=models.IntegerField(choices=[(0, 'OFF'), (1, 'ON'), (2, 'Starting'), (3, 'Pending'), (4, 'shutting off')], default=0),
        ),
    ]
