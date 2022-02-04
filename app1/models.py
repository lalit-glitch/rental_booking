from django.db import models

class Customer(models.Model):
    customer_name=models.CharField(max_length=60)
    phone_no=models.CharField(max_length=10)
    email=models.CharField(max_length=70)

class List(models.Model):
    vehicle_name=models.CharField(max_length=100)
    inventory=models.IntegerField()

class Rental(models.Model):
    custom_name=models.CharField(max_length=100)
    rental_date=models.DateField()
    return_date=models.DateField()
    vehicle_type = models.CharField(max_length=100)




    


