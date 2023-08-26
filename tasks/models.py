from django.db import models
from office.models import Team
# Create your models here.

class Task(models.Model):
    team=models.ForeignKey(Team,on_delete=models.CASCADE,default=None)
    date_assigned=models.DateField()
    completion_date=models.DateField()
    task_desc=models.CharField(max_length=500)
    status=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)
    


    def __str__(self):
        return f"{self.team}"
    

    def get_status(self):
        return "Yes" if self.status else ""
    
