# Generated by Django 4.2.3 on 2023-07-18 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('precio_seguro', models.DecimalField(decimal_places=2, max_digits=18)),
                ('precio_dependiente', models.DecimalField(decimal_places=2, max_digits=18)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_fin', models.DateTimeField()),
                ('estado', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PlanPago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_vencimiento', models.DateTimeField()),
                ('monto', models.DecimalField(decimal_places=2, max_digits=18)),
                ('contrato', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='plan_pago', to='contrato.contrato')),
            ],
        ),
    ]