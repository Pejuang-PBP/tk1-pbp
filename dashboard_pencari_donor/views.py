from django.shortcuts import render, HttpResponse
from django.core import serializers

from .models import Notifications

# Create your views here.
def index(request):
  return render(request, 'index_pencari_donor.html')

def get_notifications(request):
  if request.user.is_authenticated:
    notifications = Notifications.objects.filter(user=request.user)
    json_data = serializers.serialize("json", notifications)

    return HttpResponse(json_data, content_type="application/json")
  return HttpResponse("You are not logged in.", content_type="text/plain")