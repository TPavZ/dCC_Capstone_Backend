# Generated by Django 4.0.2 on 2022-02-08 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='prefix',
            field=models.CharField(default='Mr', max_length=5),
            preserve_default=False,
        ),
    ]
