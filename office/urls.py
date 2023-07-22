# office/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('enter/', views.enter_employee, name='enter_employee'),
    path('exit/', views.exit_employee, name='exit_employee'),
    path('create/',views.create_employee_profile,name='create_employee_profile'),
    path('dashboard/',views.dashboard,name="dashboard"),
    # Add other URL patterns for your views here
]
