# Generated by Django 4.0.2 on 2022-02-09 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0008_alter_vehicle_drive_type_alter_vehicle_engine_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='drive_type',
            field=models.CharField(blank=True, choices=[('AWD', 'AWD'), ('4WD', '4WD'), ('FWD', 'FWD'), ('RWD', 'RWD')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='engine_size',
            field=models.CharField(blank=True, choices=[('4 Cylinder', '4 Cylinder'), ('6 Cylinder', '6 Cylinder'), ('8 Cylinder', '8 Cylinder'), ('10 Cylinder', '10 Cylinder'), ('12 Cylinder', '12 Cylinder'), ('Other', 'Other')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='fuel_type',
            field=models.CharField(blank=True, choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Electric', 'Electric'), ('Other', 'Other')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='transmission_type',
            field=models.CharField(blank=True, choices=[('Automatic', 'Automatic'), ('Manual', 'Manual'), ('CVT', 'CVT')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='trim',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]