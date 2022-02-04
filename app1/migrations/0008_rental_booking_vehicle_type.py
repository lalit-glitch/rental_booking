# Generated by Django 3.2.7 on 2022-02-03 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_remove_rental_booking_vehicle_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='rental_booking',
            name='vehicle_type',
            field=models.CharField(choices=[('bi', 'bike'), ('ca', 'car'), ('bot', 'boat'), ('va', 'van'), ('scoot', 'scooter')], max_length=50, null=True),
        ),
    ]
