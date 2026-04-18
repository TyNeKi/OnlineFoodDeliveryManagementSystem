from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback_app_view, name='feedback_app'),
]