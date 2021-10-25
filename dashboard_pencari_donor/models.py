import django.utils.timezone
from django.db import models
from django.contrib.auth.models import User

from datetime import date


# Create your models here.
class Notifications(models.Model) :
    title = models.CharField(max_length=50)
    message = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(default=django.utils.timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
