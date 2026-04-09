from django.db import models

class Delivery(models.Model):
    order = models.OneToOneField('orders.Order', on_delete=models.CASCADE)
    driver = models.ForeignKey('accounts.Driver', on_delete=models.SET_NULL, null=True)
    pickupTime = models.DateTimeField(null=True, blank=True)
    deliveryTime = models.DateTimeField(null=True, blank=True)
    deliveryStatus = models.CharField(max_length=50)

class Review(models.Model):
    customer = models.ForeignKey('accounts.Customer', on_delete=models.CASCADE)
    restaurant = models.ForeignKey('restaurant.Restaurant', on_delete=models.CASCADE)
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    reviewDate = models.DateTimeField(auto_now_add=True)

class Complaint(models.Model):
    customer = models.ForeignKey('accounts.Customer', on_delete=models.CASCADE)
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE)
    admin = models.ForeignKey('accounts.Admin', on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    complaintDate = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)