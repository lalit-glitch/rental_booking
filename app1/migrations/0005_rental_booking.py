# Generated by Django 3.2.7 on 2022-02-03 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='rental_booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('rental_date', models.DateField()),
                ('return_date', models.DateField(blank=True, null=True)),
                ('vehicle_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.list')),
            ],
        ),
    ]
