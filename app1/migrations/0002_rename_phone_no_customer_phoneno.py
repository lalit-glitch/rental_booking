# Generated by Django 3.2.7 on 2022-01-31 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='phone_no',
            new_name='phoneno',
        ),
    ]