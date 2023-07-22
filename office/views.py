
from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee, EntryExitRecord
from datetime import datetime

from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee, EntryExitRecord
from datetime import datetime

# ...

def enter_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            employee_id = form.cleaned_data['employee_id']

            try:
                employee = Employee.objects.get(employee_id=employee_id)
            except Employee.DoesNotExist:
                employee = None

            if employee:
                entry_time = datetime.now()
                print(f"Employee {employee_id} entered at {entry_time}")
                # Create an EntryExitRecord for the employee with the entry time
                EntryExitRecord.objects.create(employee=employee, entry_time=entry_time)
            else:
                # Redirect to create_employee_profile view
                return redirect('create_employee_profile')

            return redirect('index')

    else:
        form = EmployeeForm()

    return render(request, 'office/enter_employee.html', {'form': form})

# ...


def exit_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            employee_id = form.cleaned_data['employee_id']

            try:
                employee = Employee.objects.get(employee_id=employee_id)
            except Employee.DoesNotExist:
                employee = None

            if employee:
                exit_time = datetime.now()
                # Retrieve the most recent EntryExitRecord for the employee and update the exit_time
                entry_exit_record = EntryExitRecord.objects.filter(employee=employee).latest('entry_time')
                entry_exit_record.exit_time = exit_time
                entry_exit_record.save()
            else:
                return redirect('create_employee_profile')
                # Employee with the given ID does not exist

            return redirect('index')

    else:
        form = EmployeeForm()

    return render(request, 'office/exit_employee.html', {'form': form})

def index(request):
    return render(request, 'office/index.html')

def create_employee_profile(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            employee_id = form.cleaned_data['employee_id']

            try:
                employee = Employee.objects.get(employee_id=employee_id)
            except Employee.DoesNotExist:
                employee = None

            if employee:
                # Employee with the given ID already exists
                return render(request, 'office/create_employee_profile.html', {'form': form, 'error_message': 'Employee with this ID already exists'})

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            entry_time = datetime.now()
            exit_time = None

            # Create a new employee with the provided details
            Employee.objects.create(employee_id=employee_id, first_name=first_name, last_name=last_name)

            return redirect('index')

    else:
        form = EmployeeForm()

    return render(request, 'office/create_employee_profile.html', {'form': form})

def dashboard(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')

        try:
            employee = Employee.objects.get(employee_id=employee_id)
            entry_exit_records = EntryExitRecord.objects.filter(employee=employee)
        except Employee.DoesNotExist:
            entry_exit_records = None

        return render(request, 'office/dashboard.html', {'entry_exit_records': entry_exit_records,'employee':'employee'})

    return render(request, 'office/dashboard.html')
