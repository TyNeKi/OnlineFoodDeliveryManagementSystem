from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='restaurant_index'),
    path('addNewRestaurant/', views.add_new_restaurant, name='add_new_restaurant'),
    path('addNewCategory/', views.add_new_category, name='add_new_category'),
    path('addNewMenu/', views.add_new_menu, name='add_new_menu'),
    path('addNewMenuItem/', views.add_new_menu_item, name='add_new_menu_item'),
]
