# office/views.py

from django.shortcuts import render, redirect
from .models import Employee
from datetime import datetime
# office/forms.py

from .forms import EmployeeForm

def enter_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            employee_id = request.POST['employee_id']

            # Check if an employee with the given ID exists
            try:
                employee = Employee.objects.get(employee_id=employee_id)
            except Employee.DoesNotExist:
                employee = None

            entry_time = datetime.now()

            if employee:
                # If the employee already has an exit_time recorded for today, only update entry_time
                if employee.exit_time and employee.exit_time.date() == entry_time.date():
                    employee.entry_time = entry_time
                    employee.save()
                else:
                    employee.entry_time = entry_time
                    employee.save()
            else:
                # Create a new employee with entry time
                employee = Employee(first_name=first_name, last_name=last_name, employee_id=employee_id, entry_time=entry_time)
                employee.save()

            return redirect('enter_employee')

    else:
        form = EmployeeForm()

    return render(request, 'office/enter_employee.html', {'form': form})


def exit_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            employee_id = request.POST['employee_id']

            # Check if an employee with the given ID exists
            try:
                employee = Employee.objects.get(employee_id=employee_id)
            except Employee.DoesNotExist:
                employee = None

            exit_time = datetime.now()

            if employee:
                # If the employee already has an entry_time recorded for today, only update exit_time
                if employee.entry_time and employee.entry_time.date() == exit_time.date():
                    employee.exit_time = exit_time
                    employee.save()
                else:
                    employee.exit_time = exit_time
                    employee.save()
            else:
                # Employee with the given ID does not exist
                return render(request, 'office/exit_employee.html', {'form': form, 'error_message': 'Employee not found'})

            return redirect('exit_employee')

    else:
        form = EmployeeForm()

    return render(request, 'office/exit_employee.html', {'form': form})


def index(request):
    return render(request, 'office/index.html')