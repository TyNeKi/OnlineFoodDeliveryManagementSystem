from django import forms
from .models import Order, OrderItem, TempUser


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customerID', 'restaurantID', 'totalAmount', 'deliveryAddress', 'orderStatus']


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['itemID', 'quantity', 'subTotal']

class TempUserForm(forms.ModelForm):
    class Meta:
        model = TempUser
        fields = ['username', 'password', 'firstName', 'lastName']