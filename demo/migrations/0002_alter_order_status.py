# Generated by Django 4.0.5 on 2023-08-06 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default='pending', max_length=250),
        ),
    ]