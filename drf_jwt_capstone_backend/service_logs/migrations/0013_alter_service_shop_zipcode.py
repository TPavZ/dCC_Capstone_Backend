# Generated by Django 4.0.2 on 2022-03-02 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_logs', '0012_alter_service_shop_city_alter_service_shop_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='shop_zipcode',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
