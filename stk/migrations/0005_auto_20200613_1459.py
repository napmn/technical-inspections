# Generated by Django 2.2.11 on 2020-06-13 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stk', '0004_auto_20200613_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='stk_id',
            field=models.IntegerField(db_index=True, unique=True),
        ),
        migrations.AlterField(
            model_name='stkinspection',
            name='stk_id',
            field=models.IntegerField(db_column='stk_id'),
        ),
        migrations.RenameField(
            model_name='stkinspection',
            old_name='stk_id',
            new_name='station'
        ),
        migrations.AlterField(
            model_name='stkinspection',
            name='station',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='stk.Station', to_field='stk_id'),
            preserve_default=False,
        )
    ]
