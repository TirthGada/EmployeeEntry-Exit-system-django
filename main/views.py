from django.shortcuts import render
from office.forms import EmployeeForm
def main_page(request):
    return render(request, 'main/main_page.html')

def app1_page(request):
    return render(request, 'office/index.html')

def app2_page(request):
    form=EmployeeForm()
    return render(request, 'tasks/index.html')
