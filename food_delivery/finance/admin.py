from django.contrib import admin
from .models import Promotion, Payment, Refund

admin.site.register(Promotion)
admin.site.register(Payment)
admin.site.register(Refund)