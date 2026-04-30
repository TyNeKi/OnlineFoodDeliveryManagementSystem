from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('admin/new/', views.add_admin_view, name='add_admin'),
    path('admin/', admin.site.urls),
    path('YourAppName/YourAddNewRecord/', views.add_admin_view, name='add_admin_alias'),

    # Authentication URLs
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    
    # Profile URLs
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),
    
    # Legacy URLs
    path('index/', views.index_view, name='index_alias'),
]
