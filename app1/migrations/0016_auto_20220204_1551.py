# Generated by Django 3.2.7 on 2022-02-04 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_alter_rental_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone_no',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterModelTable(
            name='rental',
            table=None,
        ),
    ]
