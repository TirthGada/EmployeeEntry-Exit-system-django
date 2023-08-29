
from django.contrib import admin
from .models import Team,Employee,Reward,Senior,EntryExitRecord,LeaveApplication

admin.site.register(Employee)
admin.site.register(EntryExitRecord)
admin.site.register(LeaveApplication)
admin.site.register(Senior)
admin.site.register(Reward)
admin.site.register(Team)