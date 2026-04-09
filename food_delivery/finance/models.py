from django.db import models

class Promotion(models.Model):
    promoCode = models.CharField(max_length=20, unique=True)
    discountPercentage = models.DecimalField(max_digits=5, decimal_places=2)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    status = models.CharField(max_length=20)

class Payment(models.Model):
    order = models.OneToOneField('orders.Order', on_delete=models.CASCADE)
    promo = models.ForeignKey(Promotion, on_delete=models.SET_NULL, null=True, blank=True)
    paymentMethod = models.CharField(max_length=50)
    paymentDate = models.DateTimeField(auto_now_add=True)
    paymentStatus = models.CharField(max_length=50)
    transactionReference = models.CharField(max_length=100, unique=True)

class Refund(models.Model):
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE)
    admin = models.ForeignKey('accounts.Admin', on_delete=models.SET_NULL, null=True)
    refundAmount = models.DecimalField(max_digits=10, decimal_places=2)
    refundDate = models.DateTimeField(auto_now_add=True)
    refundStatus = models.CharField(max_length=50)