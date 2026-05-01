from django.contrib import admin
from django.urls import path, include
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # The empty string '' MUST point to index_view
    path('', views.index_view, name='index'),

    # The 'login/' string MUST point to login_view
    path('login/', views.login_view, name='login'),
    
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('add_record/', views.add_record_view, name='add_record'),

    path('', include('restaurant.urls')),
]
