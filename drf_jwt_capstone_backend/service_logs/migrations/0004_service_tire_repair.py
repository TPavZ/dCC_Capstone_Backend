# Generated by Django 4.0.2 on 2022-02-11 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_logs', '0003_alter_service_other_services'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='tire_repair',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]