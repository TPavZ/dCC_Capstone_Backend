# Generated by Django 4.0.2 on 2022-02-09 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service_logs', '0002_service_date_service_details_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='date',
            new_name='service_date',
        ),
    ]
