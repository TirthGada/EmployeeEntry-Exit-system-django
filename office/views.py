
from django.shortcuts import render, redirect
from .forms import EmployeeForm,LoginForm
from .models import Employee, EntryExitRecord,Senior
from datetime import datetime
from django.core.mail import send_mail
from datetime import timedelta
from .models import Employee, LeaveApplication,Reward
from .forms import LeaveApplicationForm,RewardForm
from django.db.models import F
from django.db.models.functions import TruncDate
from django.contrib.auth import authenticate, login




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

                #first_name = employee.first_name
                #last_name = employee.last_name
                #email = f"{first_name.lower()}{last_name.lower()}1@gmail.com"
                #send_email_to_employee(first_name, last_name, email)
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
        first_name=None
        last_name=None
        try:
            employee = Employee.objects.get(employee_id=employee_id)
            entry_exit_records = EntryExitRecord.objects.filter(employee=employee)
        except Employee.DoesNotExist:
            entry_exit_records = None

        return render(request, 'office/dashboard.html', {'entry_exit_records': entry_exit_records,'employee':'employee'})

    return render(request, 'office/dashboard.html')





def send_email_to_employee(first_name, last_name, email):
    subject = 'Office Entry Notification'
    message = f'Hello {first_name} {last_name},\n\nThis is to notify you that you have entered the office premises.\n\nThank you.\n'
    from_email = 'tirthgada91@gmail.com' 
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)




def apply_leave(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        start_date = request.POST.get('start_date')  # Corrected to use parentheses for .get()
        end_date = request.POST.get('end_date')  # Corrected to use parentheses for .get()
        reason = request.POST.get('reason')  # Corrected to use parentheses for .get()

        try:
            employee = Employee.objects.get(employee_id=employee_id)
            # entry_exit_records = EntryExitRecord.objects.filter(employee=employee)  # No need for this line
        except Employee.DoesNotExist:
            employee = None
            # entry_exit_records = None  # No need for this line

        if employee:
            LeaveApplication.objects.create(employee=employee, start_date=start_date, end_date=end_date, reason=reason)
            return redirect('')
        else:
            return redirect('create_employee_profile')

    else:
        form = LeaveApplicationForm()
        return render(request, 'office/apply_leave.html', {'form': form})



def senior_dashboard(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        senior_id = request.POST.get('senior_id')
        password = request.POST.get('password')  # Corrected to use parentheses for .get()

        try:
            sen = Senior.objects.get(senior_id=senior_id, password=password)
            # entry_exit_records = EntryExitRecord.objects.filter(employee=employee)  # No need for this line
        except Senior.DoesNotExist:
            sen = None
            # entry_exit_records = None  # No need for this line

        if sen:
            pending_leave_applications = LeaveApplication.objects.filter(leave_approved=False, leave_rejected=False)
            return render(request, 'office/senior_dashboard.html', {'pending_leave_applications': pending_leave_applications,'senior_id':senior_id})
        else:
            return render(request, 'office/login.html', {'login_form': login_form, 'error_message': 'Invalid senior ID or password.'})

    else:
        login_form = LoginForm()
        return render(request, 'office/login.html', {'login_form': login_form})










def approve_leave(request, leave_id):
    try:
        leave_application = LeaveApplication.objects.get(id=leave_id)
    except LeaveApplication.DoesNotExist:
        leave_application = None

    if leave_application:
        if request.method == 'POST':
            if 'approve' in request.POST:
                leave_application.leave_approved = True
                leave_application.leave_rejected = False
            elif 'reject' in request.POST:
                leave_application.leave_approved = False
                leave_application.leave_rejected = True
            leave_application.save()
        return redirect('senior_dashboard')
    else:
        return redirect('senior_dashboard')
    


def status(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')

        try:
            employee = Employee.objects.get(employee_id=employee_id)
            records = LeaveApplication.objects.filter(employee=employee)
        except Employee.DoesNotExist:
            records = None

        return render(request, 'office/status.html', {'records': records})

    return render(request, 'office/status.html')



def reward(request):
    if request.method == 'POST':
        form = RewardForm(request.POST)
        if form.is_valid():
            employee_id = form.cleaned_data['employee_id']

            try:
                employee = Employee.objects.get(employee_id=employee_id)
            except Employee.DoesNotExist:
                employee = None

            if employee:
                rewardprize = Reward.objects.filter(employee=employee)
                return render(request, 'office/reward.html', {'rewardprize': rewardprize})

    else:
        form = RewardForm()

    return render(request, 'office/reward.html', {'form': form})