from django.db import models

class Delivery(models.Model):
    DELIVERY_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('picked_up', 'Picked Up'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
        ('failed', 'Failed'),
    ]

    deliveryID = models.AutoField(primary_key=True)
    orderID = models.ForeignKey('orders.Order', on_delete=models.CASCADE)
    driverID = models.ForeignKey('accounts.Driver', on_delete=models.SET_NULL, null=True, blank=True)
    pickupTime = models.DateTimeField(null=True, blank=True)
    deliveryTime = models.DateTimeField(null=True, blank=True)
    deliveryStatus = models.CharField(max_length=20, choices=DELIVERY_STATUS_CHOICES)

    def __str__(self):
        return "Delivery " + str(self.deliveryID)

class Review(models.Model):
    reviewID = models.AutoField(primary_key=True)
    customerID = models.ForeignKey('accounts.Customer', on_delete=models.CASCADE)
    restaurantID = models.ForeignKey('restaurant.Restaurant', on_delete=models.CASCADE)
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    reviewDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Review " + str(self.reviewID)

class Complaint(models.Model):
    COMPLAINT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('under_review', 'Under Review'),
        ('resolved', 'Resolved'),
        ('rejected', 'Rejected'),
    ]

    complaintID = models.AutoField(primary_key=True)
    customerID = models.ForeignKey('accounts.Customer', on_delete=models.CASCADE)
    orderID = models.ForeignKey('orders.Order', on_delete=models.CASCADE)
    adminID = models.ForeignKey('accounts.Admin', on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    complaintDate = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=COMPLAINT_STATUS_CHOICES)

    def __str__(self):
        return "Complaint " + str(self.complaintID)