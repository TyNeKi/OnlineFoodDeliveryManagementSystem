from django.contrib import admin
from django.urls import path, include
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index_view, name='index'),

    path('login/', views.login_view, name='login'),
    path('feedback/', include('feedback.urls')),
]