# office/forms.py

from django import forms

class EmployeeForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    employee_id = forms.CharField(max_length=10)

