from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='feedback_index'),
    path('addNewComplaint/', views.add_new_complaint_view, name='feedback_add_new_complaint'),
    path('legacy/', views.feedback_app_view, name='feedback_app'),
]