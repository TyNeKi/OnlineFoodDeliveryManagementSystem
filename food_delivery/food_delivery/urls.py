from django.contrib import admin
from django.urls import path, include
from accounts import views
from orders.views import IndexView, HomeView

urlpatterns = [
    path('admin/', admin.site.urls),

    # The empty string '' MUST point to index_view
    path('', IndexView.as_view(), name='index'),

    path('home/', HomeView.as_view(), name='home'),

    path('orders/', include('orders.urls')),
    # The 'login/' string MUST point to login_view
    #path('login/', views.login_view, name='login'),
]