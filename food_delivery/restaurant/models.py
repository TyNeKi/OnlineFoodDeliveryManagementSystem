from django.db import models

class Restaurant(models.Model):

    STATUS_CHOICES = [
        ('open', 'Open'),
        ('closed', 'Closed'),
    ]

    restaurantID = models.AutoField(primary_key=True)
    adminID = models.ForeignKey('accounts.Admin', on_delete=models.CASCADE)
    restaurantName = models.CharField(max_length=100)
    address = models.TextField()
    phoneNumber = models.CharField(max_length=15)
    email = models.EmailField()
    openingTime = models.TimeField()
    closingTime = models.TimeField()
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return self.restaurantName


class Category(models.Model):

    categoryID = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.categoryName


class Menu(models.Model):

    menuID = models.AutoField(primary_key=True)
    restaurantID = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
    menuName = models.CharField(max_length=100)
    description = models.TextField()
    lastUpdateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.menuName


class MenuItem(models.Model):

    itemID = models.AutoField(primary_key=True)
    menuID = models.ForeignKey('Menu', on_delete=models.CASCADE)
    categoryID = models.ForeignKey('Category', on_delete=models.CASCADE)
    itemName = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    availabilityStatus = models.BooleanField(default=True)

    def __str__(self):
        return self.itemName