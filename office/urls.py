# office/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('enter/', views.enter_employee, name='enter_employee'),
    path('exit/', views.exit_employee, name='exit_employee'),
    path('create/',views.create_employee_profile,name='create_employee_profile'),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('apply_leave/', views.apply_leave, name='apply_leave'),
    path('senior_dashboard/', views.senior_dashboard, name='senior_dashboard'),
    path('approve_leave/<int:leave_id>/', views.approve_leave, name='approve_leave'),
    path('status/',views.status,name='status'),
    path('reward/',views.reward,name='reward')
]

