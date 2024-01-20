from django.db import models

class TaskAddModel(models.Model):
    title = models.CharField(primary_key = True, max_length = 30)
    description = models.CharField(max_length = 300)
    is_completed = models.BooleanField(default = False)
    def __str__(self):
        return f"{self.title}"
    def status(self):
        return 'Complete' if self.is_completed else 'Incomplete'
    
    
