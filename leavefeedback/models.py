from django.db import models

# Create your models here.
class LeaveModel(models.Model):
    email = models.CharField(max_length=100)
    good = models.CharField(max_length=1000)
    improve = models.CharField(max_length=1000)
