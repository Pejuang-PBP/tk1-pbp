import django.utils.timezone
from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Notifications(models.Model) :
    title = models.CharField(max_length=50)
    message = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(default=django.utils.timezone.now)
    status = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
