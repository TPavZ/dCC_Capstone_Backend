# Generated by Django 4.0.2 on 2022-02-09 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0002_alter_vehicle_fuel_type_alter_vehicle_trim'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='engine_size',
        ),
    ]
