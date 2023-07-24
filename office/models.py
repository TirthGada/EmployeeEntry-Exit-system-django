from django.db import models
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class EntryExitRecord(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    entry_time = models.DateTimeField()
    exit_time = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.employee.first_name}"

class LeaveApplication(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    leave_approved = models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)
    leave_rejected = models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)

    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name} - {self.start_date} to {self.end_date}"

    def get_leave_approved_display(self):
        return "Yes" if self.leave_approved else ""

    def get_leave_rejected_display(self):
        return "Yes" if self.leave_rejected else ""


class Senior(models.Model):
    senior_id=models.CharField(max_length=10)
    password=models.CharField(max_length=20)