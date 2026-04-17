from django.urls import path
from .views import index, add_new_order

urlpatterns = [

    # The empty string '' MUST point to index_view
    path('',index, name='index'),
    path('AddNewOrder/',add_new_order, name='add_new_order'),
]