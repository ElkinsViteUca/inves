# Generated by Django 4.0.2 on 2022-03-24 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appnomina', '0006_alter_empleado_options_alter_empleado_cedula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='departamento',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]
