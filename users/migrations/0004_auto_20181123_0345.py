# Generated by Django 2.1.2 on 2018-11-23 03:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20181123_0326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='date_created',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
