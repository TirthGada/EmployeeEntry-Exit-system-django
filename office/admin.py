
from django.contrib import admin
from .models import Employee,EntryExitRecord,LeaveApplication

admin.site.register(Employee)
admin.site.register(EntryExitRecord)
admin.site.register(LeaveApplication)