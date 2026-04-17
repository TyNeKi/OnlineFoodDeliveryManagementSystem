from django.db import models

ORDER_STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Preparing', 'Preparing'),
    ('Out for Delivery', 'Out for Delivery'),
    ('Delivered', 'Delivered'),
    ('Cancelled', 'Cancelled'),
]

class Order(models.Model):
    orderID = models.AutoField(primary_key=True)
    customerID = models.ForeignKey('accounts.Customer', on_delete=models.CASCADE)
    restaurantID = models.ForeignKey('restaurant.Restaurant', on_delete=models.CASCADE)
    orderDate = models.DateTimeField(auto_now_add=True)
    orderStatus = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='Pending')
    totalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    deliveryAddress = models.TextField()

    def __str__(self):
        return "Order " + str(self.orderID)

class OrderItem(models.Model):
    orderItemID = models.AutoField(primary_key=True)
    orderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    itemID = models.ForeignKey('restaurant.MenuItem', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    subTotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return "OrderItem " + str(self.orderItemID)