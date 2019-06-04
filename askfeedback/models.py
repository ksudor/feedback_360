from django.db import models
from datetime import date

# Create your models here.
class AskModel(models.Model):
    email = models.CharField(max_length=100)
    emails = models.CharField(max_length=1000)
    deadline = models.DateField(default=date.today)
