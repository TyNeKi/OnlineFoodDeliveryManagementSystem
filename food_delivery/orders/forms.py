from django import forms
from .models import Order, OrderItem, TempUser


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['restaurantID', 'deliveryAddress']
        labels = {
            'restaurantID': 'Restaurant',
            'deliveryAddress': 'Delivery Address',
        }

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['itemID', 'quantity']
        labels = {
            'itemID': 'Items',
            'quantity': 'Quantity',
        }

class TempUserForm(forms.ModelForm):
    class Meta:
        model = TempUser
        fields = ['username', 'password', 'firstName', 'lastName']