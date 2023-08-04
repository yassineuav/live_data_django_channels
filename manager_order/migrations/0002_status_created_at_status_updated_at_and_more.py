# Generated by Django 4.0.5 on 2023-08-03 03:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('manager_order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='status',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='manager_order.status'),
        ),
        migrations.AlterField(
            model_name='status',
            name='description',
            field=models.TextField(),
        ),
    ]
