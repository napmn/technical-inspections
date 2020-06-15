# Generated by Django 2.2.11 on 2020-06-14 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stk', '0006_auto_20200614_0833'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrecalculatedStatistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(blank=True, max_length=255, null=True)),
                ('number_of_stations', models.IntegerField()),
                ('pass_rate', models.DecimalField(decimal_places=3, max_digits=6)),
                ('inspected_vehicles_number', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='stkinspection',
            name='repeated',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='stkinspection',
            name='inspection_type',
            field=models.CharField(choices=[('Technická silniční kontrola', 'Technická silniční kontrola'), ('ADR', 'ADR'), ('Pravidelná', 'Pravidelná'), ('Před schvál. tech. způsob. vozidla', 'Před schvál. tech. způsob. vozidla'), ('Před registrací', 'Před registrací'), ('Nařízená technická prohlídka', 'Nařízená technická prohlídka'), ('Evidenční kontrola', 'Evidenční kontrola'), ('Na žádost zákazníka', 'Na žádost zákazníka')], db_index=True, max_length=255),
        ),
    ]
