# Generated by Django 4.0.2 on 2022-02-08 21:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin', models.CharField(max_length=17)),
                ('year', models.IntegerField()),
                ('make', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=100)),
                ('trim', models.CharField(max_length=100)),
                ('engine_size', models.IntegerField()),
                ('transmission_type', models.CharField(max_length=50)),
                ('drive_type', models.IntegerField()),
                ('fuel_type', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
