from django.urls import path
from . import views

urlpatterns = [
    path('<str:employee_id>/',views.employee_profile,name='employee_profile'),
]