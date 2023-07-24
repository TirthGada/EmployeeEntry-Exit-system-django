
from django.contrib import admin
from .models import Employee,Senior,EntryExitRecord,LeaveApplication

admin.site.register(Employee)
admin.site.register(EntryExitRecord)
admin.site.register(LeaveApplication)
admin.site.register(Senior)