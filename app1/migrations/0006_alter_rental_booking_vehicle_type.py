# Generated by Django 3.2.7 on 2022-02-03 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_rental_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental_booking',
            name='vehicle_type',
            field=models.CharField(max_length=100),
        ),
    ]