# Generated by Django 4.0.2 on 2022-02-14 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_logs', '0005_alter_service_major_repairs'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='current_mileage',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
