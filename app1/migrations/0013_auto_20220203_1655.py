# Generated by Django 3.2.7 on 2022-02-03 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_alter_rental_booking_vehicle_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rental_booking',
            name='customer_name',
        ),
        migrations.RemoveField(
            model_name='rental_booking',
            name='rental_date',
        ),
        migrations.RemoveField(
            model_name='rental_booking',
            name='return_date',
        ),
        migrations.RemoveField(
            model_name='rental_booking',
            name='vehicle_type',
        ),
        migrations.AlterModelTable(
            name='rental_booking',
            table='Rental_booking',
        ),
    ]