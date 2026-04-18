from django.db import models

class Admin(models.Model):

    ACCESS_LEVEL_CHOICES = [
        ('full', 'Full Access'),
        ('limited', 'Limited Access'),
    ]

    adminID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50)
    accessLevel = models.CharField(max_length=20, choices=ACCESS_LEVEL_CHOICES)

    def __str__(self):
        return self.name

class Customer(models.Model):
    ACCOUNT_STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    customerID = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phoneNumber = models.CharField(max_length=15)
    address = models.TextField()
    registrationDate = models.DateTimeField(auto_now_add=True)
    accountStatus = models.CharField(max_length=20, choices=ACCOUNT_STATUS_CHOICES)

    def __str__(self):
        return self.firstName + " " + self.lastName

class Driver(models.Model):
    AVAILABILITY_CHOICES = [
        ('available', 'Available'),
        ('busy', 'Busy'),
        ('offline', 'Offline'),
    ]

    driverID = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=15)
    licenseNumber = models.CharField(max_length=50, unique=True)
    vehicleType = models.CharField(max_length=50)
    availabilityStatus = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)

    def __str__(self):
        return self.firstName + " " + self.lastName