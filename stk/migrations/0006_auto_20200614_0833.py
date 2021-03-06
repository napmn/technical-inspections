# Generated by Django 2.2.11 on 2020-06-14 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stk', '0005_auto_20200613_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stkinspection',
            name='emission_result',
            field=models.CharField(choices=[('vyhovuje', 'vyhovuje'), ('nevyhovuje', 'nevyhovuje'), ('částečně vyhovuje', 'částečně vyhovuje')], db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='stkinspection',
            name='inspection_result',
            field=models.CharField(choices=[('Částečně způsobilé', 'Způsobilé'), ('Nezpůsobilé', 'Nezpůsobilé'), ('Částečně způsobilé', 'Částečně způsobilé')], db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='stkinspection',
            name='inspection_type',
            field=models.CharField(choices=[('TSK - Opakovaná', 'TSK - Opakovaná'), ('Nařízená technická prohlídka', 'Nařízená technická prohlídka'), ('pravidelná', 'pravidelná'), ('Evidenční kontrola', 'Evidenční kontrola'), ('Technická silniční kontrola', 'Technická silniční kontrola'), ('ADR', 'ADR'), ('opakovaná', 'opakovaná'), ('TSK - Opakovaná po DN', 'TSK - Opakovaná po DN'), ('Před schvál. tech. způsob. vozidla', 'Před schvál. tech. způsob. vozidla'), ('ADR - opakovaná', 'ADR - opakovaná'), ('Před schvál. tech. způsob. vozidla - opakovaná', 'Před schvál. tech. způsob. vozidla - opakovaná'), ('Před registrací - opakovaná', 'Před registrací - opakovaná'), ('Před registrací', 'Před registrací'), ('Na žádost zákazníka', 'Na žádost zákazníka')], db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_type',
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_vendor',
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AddIndex(
            model_name='vehicle',
            index=models.Index(fields=['vehicle_vendor', 'vehicle_model'], name='vehicle_vendor_model_index'),
        ),
    ]
