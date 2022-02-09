# Generated by Django 4.0.2 on 2022-02-09 21:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shops', '0002_shop_city_shop_contact_first_name_and_more'),
        ('vehicles', '0009_alter_vehicle_drive_type_alter_vehicle_engine_size_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_date', models.DateField(auto_now=True)),
                ('service_grand_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=7)),
                ('service_details', models.TextField(blank=True, null=True)),
                ('shop', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shops.shop')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicles.vehicle')),
            ],
        ),
    ]
