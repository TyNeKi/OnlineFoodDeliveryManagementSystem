from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='restaurant_index'),
    path('addNewRestaurant', views.add_new_restaurant, name='add_new_restaurant'),
    path('addNewCategory', views.add_new_category, name='add_new_category'),
    path('addNewMenu', views.add_new_menu, name='add_new_menu'),
    path('addNewMenuItem', views.add_new_menu_item, name='add_new_menu_item'),
    path('index/', views.index, name='restaurant_index_slash'),
    path('addNewRestaurant/', views.add_new_restaurant, name='add_new_restaurant_slash'),
    path('addNewCategory/', views.add_new_category, name='add_new_category_slash'),
    path('addNewMenu/', views.add_new_menu, name='add_new_menu_slash'),
    path('addNewMenuItem/', views.add_new_menu_item, name='add_new_menu_item_slash'),
]
