from django.contrib import admin
from .models import Complaint, Delivery, Review

admin.site.register(Complaint)
admin.site.register(Delivery)
admin.site.register(Review)
