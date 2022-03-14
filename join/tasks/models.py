from datetime import datetime
from tokenize import group
from django.utils import timezone
from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    category = models.CharField(max_length=100, default="")
    urgency = models.CharField(max_length=100, default="")
    due_date = models.DateTimeField('dead line')
    created_at = models.DateTimeField('created at')
    group = models.CharField(max_length=100, default="")

    # def __str__(self) -> str:
    #     return self.title
    
    def created_recently(self):
        return self.created_at >= timezone.now() - datetime.timedelta(days=1)