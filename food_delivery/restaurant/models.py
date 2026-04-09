from django.db import models

class Restaurant(models.Model):
    admin = models.ForeignKey('accounts.Admin', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    address = models.TextField()
    phoneNumber = models.CharField(max_length=15)
    email = models.EmailField()
    openingTime = models.TimeField()
    closingTime = models.TimeField()
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    status = models.CharField(max_length=20)

class Category(models.Model):
    categoryName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True)

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    menuName = models.CharField(max_length=100)
    description = models.TextField()
    lastUpdateDate = models.DateTimeField(auto_now=True)

class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    itemName = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    availabilityStatus = models.BooleanField(default=True)