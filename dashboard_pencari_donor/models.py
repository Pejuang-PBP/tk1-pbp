import django.utils.timezone
from django.db import models
from django.contrib.auth.models import User
from form_pencari_donor.models import request_pencari_donor

# Create your models here.
class Notifications(models.Model):
    title = models.CharField(max_length=50)
    message = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(default=django.utils.timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_pencari_notifications')

class Report(models.Model):
    title = models.CharField(max_length=500)
    message = models.CharField(max_length=2000)
    timestamp = models.DateTimeField(default=django.utils.timezone.now)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.title}"

class Response(models.Model):
    message = models.CharField(max_length=2000)
    timestamp = models.DateTimeField(default=django.utils.timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_pencari_response')
    report = models.ForeignKey(Report, on_delete=models.CASCADE)

class Donor(models.Model):
    donor = models.OneToOneField(to=User, on_delete=models.CASCADE)
    request = models.ForeignKey(to=request_pencari_donor, on_delete=models.CASCADE)
    chosen = models.BooleanField(default=False)