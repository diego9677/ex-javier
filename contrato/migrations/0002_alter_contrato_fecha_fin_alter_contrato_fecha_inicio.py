# Generated by Django 4.2.3 on 2023-07-19 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contrato', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='fecha_fin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='fecha_inicio',
            field=models.DateField(),
        ),
    ]