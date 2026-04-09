from django.contrib import admin
from .models import Delivery, Review, Complaint

admin.site.register(Delivery)
admin.site.register(Review)
admin.site.register(Complaint)