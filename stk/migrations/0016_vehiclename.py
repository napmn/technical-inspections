# Generated by Django 2.2.13 on 2020-06-16 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stk', '0015_auto_20200615_2210'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_model', models.CharField(blank=True, db_index=True, max_length=512, null=True)),
            ],
        ),
    ]