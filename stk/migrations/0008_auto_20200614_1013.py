# Generated by Django 2.2.11 on 2020-06-14 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stk', '0007_auto_20200614_0901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='precalculatedstatistic',
            name='pass_rate',
        ),
        migrations.AddField(
            model_name='precalculatedstatistic',
            name='eligible',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='precalculatedstatistic',
            name='ineligible',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='precalculatedstatistic',
            name='partially_eligible',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='precalculatedstatistic',
            name='inspected_vehicles_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='precalculatedstatistic',
            name='number_of_stations',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='InspectionTypeStatistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inspection_type', models.CharField(choices=[('Technická silniční kontrola', 'Technická silniční kontrola'), ('ADR', 'ADR'), ('Pravidelná', 'Pravidelná'), ('Před schvál. tech. způsob. vozidla', 'Před schvál. tech. způsob. vozidla'), ('Před registrací', 'Před registrací'), ('Nařízená technická prohlídka', 'Nařízená technická prohlídka'), ('Evidenční kontrola', 'Evidenční kontrola'), ('Na žádost zákazníka', 'Na žádost zákazníka')], db_index=True, max_length=255)),
                ('repeated', models.BooleanField(default=False)),
                ('number_of_inspections', models.IntegerField(default=0)),
                ('precalculated_statistic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stk.PrecalculatedStatistic')),
            ],
        ),
    ]
