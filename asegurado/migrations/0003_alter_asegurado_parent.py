# Generated by Django 4.2.3 on 2023-07-18 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asegurado', '0002_alter_asegurado_fecha_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asegurado',
            name='parent',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='asegurado', to='asegurado.asegurado'),
        ),
    ]
