# Generated by Django 4.0.2 on 2022-02-09 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='fuel_type',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='trim',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
