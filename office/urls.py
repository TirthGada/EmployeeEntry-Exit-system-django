# office/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('enter/', views.enter_employee, name='enter_employee'),
    path('exit/', views.exit_employee, name='exit_employee'),
    # Add other URL patterns for your views here
]
