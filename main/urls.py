from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('office/', views.app1_page, name='app1_page'),
    path('tasks/', views.app2_page, name='app2_page'),
    # Add more app URLs as needed
]
