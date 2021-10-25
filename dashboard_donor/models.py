import django.utils
from django.db import models
from datetime import date

# Create your models here.
class Notifications(models.Model) :
    title = models.CharField(max_length=50)
    message = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(default=django.utils.timezone.now)
    status = models.CharField(max_length=20)