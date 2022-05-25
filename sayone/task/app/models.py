from django.db import models

# Create your models here.
class addevent(models.Model):
    event_name = models.CharField(max_length=100) 
    event_description=models.TextField()
    event_coordinator = models.CharField(max_length=100)