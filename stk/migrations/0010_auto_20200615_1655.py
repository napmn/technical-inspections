# Generated by Django 2.2.11 on 2020-06-15 16:55

import django.contrib.postgres.indexes
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stk', '0009_auto_20200614_1046'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='vehicle',
            name='vehicle_vendor_model_index',
        ),
        migrations.AlterField(
            model_name='station',
            name='region',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddIndex(
            model_name='station',
            index=django.contrib.postgres.indexes.HashIndex(fields=['region'], name='stk_station_region_62e8e1_hash'),
        ),
    ]
