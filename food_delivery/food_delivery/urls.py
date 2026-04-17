from django.contrib import admin
from django.urls import path, include
from accounts import views
from orders.views import index

urlpatterns = [
    path('admin/', admin.site.urls),

    # The empty string '' MUST point to index_view
    path('',index),

    # The 'login/' string MUST point to login_view
    path('orders/', include('orders.urls')),
    path('login/', views.login_view, name='login'),
]