from django.db import models

class Promotion(models.Model):
    PROMO_STATUS_CHOICES = [
        ('active', 'Active'),
        ('expired', 'Expired'),
    ]

    promoID = models.AutoField(primary_key=True)
    promoCode = models.CharField(max_length=20, unique=True)
    discountPercentage = models.DecimalField(max_digits=5, decimal_places=2)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    status = models.CharField(max_length=20, choices=PROMO_STATUS_CHOICES)

    def __str__(self):
        return self.promoCode

class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('card', 'Card'),
        ('online', 'Online Payment'),
    ]

    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]

    paymentID = models.AutoField(primary_key=True)
    orderID = models.ForeignKey('orders.Order', on_delete=models.CASCADE)
    promoID = models.ForeignKey(Promotion, on_delete=models.SET_NULL, null=True, blank=True)
    paymentMethod = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    paymentDate = models.DateTimeField(auto_now_add=True)
    paymentStatus = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES)
    transactionReference = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return "Payment " + str(self.paymentID)

class Refund(models.Model):
    REFUND_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('processed', 'Processed'),
    ]

    refundID = models.AutoField(primary_key=True)
    paymentID = models.ForeignKey(Payment, on_delete=models.CASCADE)
    adminID = models.ForeignKey('accounts.Admin', on_delete=models.CASCADE)
    refundAmount = models.DecimalField(max_digits=10, decimal_places=2)
    refundDate = models.DateTimeField(auto_now_add=True)
    refundStatus = models.CharField(max_length=20, choices=REFUND_STATUS_CHOICES)

    def __str__(self):
        return "Refund " + str(self.refundID)