from django.contrib import admin
from django.urls import path, include
from feedback import views as feedback_views
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', feedback_views.index_view, name='index'),
    path('login/', accounts_views.login_view, name='login'),
    path('logout/', accounts_views.logout_view, name='logout'),
    path('home/', accounts_views.home_view, name='home'),
    path('edit-profile/', accounts_views.edit_profile_view, name='edit_profile'),
    path('feedback/', include('feedback.urls')),
]