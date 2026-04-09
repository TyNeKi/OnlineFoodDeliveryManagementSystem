from django.db import models

class Admin(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50)
    accessLevel = models.CharField(max_length=50)

class Customer(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phoneNumber = models.CharField(max_length=15)
    address = models.TextField()
    registrationDate = models.DateTimeField(auto_now_add=True)
    accountStatus = models.CharField(max_length=20)

class Driver(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=15)
    licenseNumber = models.CharField(max_length=50, unique=True)
    vehicleType = models.CharField(max_length=50)
    availabilityStatus = models.CharField(max_length=20)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)