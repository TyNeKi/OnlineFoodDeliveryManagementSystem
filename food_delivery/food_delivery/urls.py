from django.contrib import admin
from django.urls import path, include
from feedback import views as feedback_views
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', feedback_views.index_view, name='index'),
    path('login/', accounts_views.login_view, name='login'),
    path('feedback/', include('feedback.urls')),
]