from django.shortcuts import render, redirect
from office.models import Employee, EntryExitRecord
from office.forms import EmployeeForm
from datetime import datetime

def login(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            employee_id = form.cleaned_data['employee_id']

            try:
                employee = Employee.objects.get(employee_id=employee_id)
            except Employee.DoesNotExist:
                employee = None

            if employee:
                return render(request, 'tasks/home.html', {'employee': employee})
            else:
                # Redirect to create_employee_profile view
                return redirect('login')

    else:
        form = EmployeeForm()

    return render(request, 'tasks/login.html', {'form': form})
