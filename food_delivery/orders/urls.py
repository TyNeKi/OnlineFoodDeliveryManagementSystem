from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import IndexView, AddNewOrderView, HomeView, LogoffView, EditProfileView

urlpatterns = [

    # The empty string '' MUST point to index_view
    path('', IndexView.as_view(), name='index'),
    path('home/', HomeView.as_view(), name='home'),
    path('AddNewOrder/', AddNewOrderView.as_view(), name='add_new_order'),
    path('logoff/', LogoffView.as_view(), name='logoff'),
    path('editprofile/', EditProfileView.as_view(), name='edit_profile'),
]