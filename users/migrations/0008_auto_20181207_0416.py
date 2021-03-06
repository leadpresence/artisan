# Generated by Django 2.1.2 on 2018-12-07 04:16

from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20181130_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerartisan',
            name='artisan_phone',
            field=models.IntegerField(validators=[users.validators.phone_validation]),
        ),
        migrations.AlterField(
            model_name='registerartisan',
            name='artisan_skill',
            field=models.CharField(choices=[('A/C Maintenace', 'A/C maintenance'), ('Plumbing', 'plumbing'), ('Hygeine-Cleaning', 'hygiene-cleaning'), ('Car-Wash', 'car wash'), ('Chef-All-Meals', 'All-Meals'), ('Chef-African', 'Chef-Afrcan'), ('Chef-Intercontinental', 'Chef-Intercontinental'), ('Electrical-Wiring', 'electrical-wiring'), ('Electrical-Electronics', 'electrical-electronics'), ('Engineering-Auto', 'engineering-auto'), ('Engineering-Generators', 'engineering-generators'), ('Driving-Trucks', 'driving-trucks'), ('Driving-HeavyDuty', 'driving-Heavy-Duty'), ('Driving-Automobile', 'driving-automobile'), ('Medicals-Nurse', 'medicals-nurse')], max_length=150),
        ),
    ]
