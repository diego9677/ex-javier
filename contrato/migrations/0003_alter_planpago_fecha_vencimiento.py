# Generated by Django 4.2.3 on 2023-07-19 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contrato', '0002_alter_contrato_fecha_fin_alter_contrato_fecha_inicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planpago',
            name='fecha_vencimiento',
            field=models.DateField(),
        ),
    ]
