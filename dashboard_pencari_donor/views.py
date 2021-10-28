from django.db import models
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from .models import Notifications
from form_pencari_donor.models import request_pencari_donor

def not_authenticated():
  return HttpResponse("You are not logged in.", content_type="text/plain")

# Create your views here.
@login_required(login_url="/login")
def index(request):
  return render(request, 'index_pencari_donor.html', { "user": request.user })
  

def get_notifications(request):
  if request.user.is_authenticated:
    notifications = Notifications.objects.filter(user=request.user)
    json_data = serializers.serialize("json", notifications)

    return HttpResponse(json_data, content_type="application/json")
  return not_authenticated()

@csrf_exempt
def get_request(request):
  if request.user.is_authenticated:
    if request.method == "GET":
      request_info = request_pencari_donor.objects.filter(user=request.user)
      json_data = serializers.serialize("json", request_info)

      return HttpResponse(json_data, content_type="application/json")
    elif request.method == "DELETE":
      requestId = request.GET.get("id")
      try:
        request_info = request_pencari_donor.objects.get(id=requestId)
        if (request_info.user == request.user):
          request_info.delete()
          return HttpResponse("Successfully deleted row.")
        else:
          return HttpResponse("You do not have the permission to remove this row.", content_type="text/plain")
      except request_pencari_donor.DoesNotExist:
        return HttpResponse("Record does not exist.", status=404)
        

  return not_authenticated()

