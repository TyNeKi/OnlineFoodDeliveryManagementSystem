from django.contrib import admin
from django.contrib.auth.models import User

from .models import Order, OrderItem, TempUser

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(TempUser)