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
