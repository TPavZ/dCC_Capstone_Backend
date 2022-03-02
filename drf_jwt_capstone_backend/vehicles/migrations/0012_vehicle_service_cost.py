# Generated by Django 4.0.2 on 2022-03-02 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0011_alter_vehicle_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='service_cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7),
        ),
    ]
