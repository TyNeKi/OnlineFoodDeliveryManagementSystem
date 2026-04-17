from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/new/', views.add_admin_view, name='add_admin'),
    path('YourAppName/YourAddNewRecord/', views.add_admin_view, name='add_admin_alias'),

    # The empty string '' MUST point to index_view
    path('', views.index_view, name='index'),

    # The 'login/' string MUST point to login_view
    path('login/', views.login_view, name='login'),
]