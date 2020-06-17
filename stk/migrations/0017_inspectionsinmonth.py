# Generated by Django 2.2.13 on 2020-06-17 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stk', '0016_vehiclename'),
    ]

    operations = [
        migrations.CreateModel(
            name='InspectionsInMonth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passed', models.IntegerField(default=0)),
                ('not_passed', models.IntegerField(default=0)),
                ('month', models.IntegerField(default=0)),
                ('precalculated_statistic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stk.PrecalculatedStatistic')),
            ],
        ),
    ]
