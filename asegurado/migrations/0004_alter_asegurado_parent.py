# Generated by Django 4.2.3 on 2023-07-18 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asegurado', '0003_alter_asegurado_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asegurado',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='asegurado', to='asegurado.asegurado'),
        ),
    ]