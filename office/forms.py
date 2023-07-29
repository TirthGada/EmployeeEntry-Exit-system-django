# office/forms.py

from django import forms
from . models import Senior

class EmployeeForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    employee_id = forms.CharField(max_length=10)

from .models import LeaveApplication

class LeaveApplicationForm(forms.Form):
    employee_id = forms.CharField(max_length=10)
    start_date=forms.DateField()
    end_date=forms.DateField()
    reason=forms.CharField(max_length=1000)


class LoginForm(forms.Form):
    senior_id = forms.CharField(max_length=10)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)

class RewardForm(forms.Form):
    employee_id=forms.CharField(max_length=20)



