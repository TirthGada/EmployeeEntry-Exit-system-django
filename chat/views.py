from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from office.models import Employee
from .models import Message
def employee_profile(request, employee_id):
    employee = get_object_or_404(Employee, employee_id=employee_id)
    
    # Retrieve messages sent by the employee
    sent_messages = employee.sent_messages.all()
    
    # Retrieve messages received by the employee
    received_messages = employee.received_messages.all()
    
    context = {
        'employee': employee,
        'sent_messages': sent_messages,
        'received_messages': received_messages
    }
    
    return render(request, 'employee_profile.html', context)
