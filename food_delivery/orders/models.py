from django.db import models

class Order(models.Model):
    customer = models.ForeignKey('accounts.Customer', on_delete=models.CASCADE)
    restaurant = models.ForeignKey('restaurant.Restaurant', on_delete=models.CASCADE)
    orderDate = models.DateTimeField(auto_now_add=True)
    orderStatus = models.CharField(max_length=50)
    totalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    deliveryAddress = models.TextField()

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey('restaurant.MenuItem', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    subTotal = models.DecimalField(max_digits=10, decimal_places=2)