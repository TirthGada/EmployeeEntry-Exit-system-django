from django.shortcuts import render

def main_page(request):
    return render(request, 'main/main_page.html')

def app1_page(request):
    return render(request, 'office/index.html')

def app2_page(request):
    return render(request, 'tasks/login.html')
