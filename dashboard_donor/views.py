from django.db import models
from django.http.response import HttpResponseRedirect, JsonResponse, HttpResponseNotFound
from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from .models import Notifications, Report, Response
from form_donor.models import request_donor
from form_pencari_donor.models import request_pencari_donor
from .forms import ReportForm
from dashboard_pencari_donor.models import Donor, Notifications as DonorNotifications

# Create your views here.

def not_authenticated():
  return HttpResponse("You are not logged in.", content_type="text/plain")


@login_required(login_url="/login")
def index(request) :
    return render(request, 'index_donor.html', { "user": request.user })


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
      request_info = request_donor.objects.filter(user=request.user)
      json_data = serializers.serialize("json", request_info)

      return HttpResponse(json_data, content_type="application/json")
    elif request.method == "DELETE":
      requestId = request.GET.get("id")
      try:
        request_info = request_donor.objects.get(id=requestId)
        if (request_info.user == request.user):
          request_info.delete()
          return HttpResponse("Successfully deleted row.")
        else:
          return HttpResponse("You do not have the permission to remove this row.", content_type="text/plain")
      except request_donor.DoesNotExist:
        return HttpResponse("Record does not exist.", status=404)
        
def report(request):
  if request.method == "POST":
    if request.user.is_authenticated:
        form = ReportForm(request.POST)
        
        if form.is_valid():
          # process the data in form.cleaned_data as required
          # ...
          # redirect to a new URL:
          obj = form.save(commit=False)
          obj.user = request.user
          obj.save()
          
          return JsonResponse({ "status": True })
        return JsonResponse({ "status": False })
    else:
      return not_authenticated()
  elif request.method == "GET" :
    if request.user.is_authenticated:
      reports = Report.objects.select_related().filter(user=request.user)
      data = []

      for thisReport in reports:
        responses = Response.objects.filter(report=thisReport)
        data.append({
          "title": thisReport.title,
          "message": thisReport.message,
          "timestamp": thisReport.timestamp,
          "replies": serializers.serialize("json", responses)
        })

      return JsonResponse(data, safe=False)
    else:
      return not_authenticated()

  return HttpResponseNotFound()

@csrf_exempt
def donors(request):
  if request.user.is_authenticated:
    if request.method == "GET":
      requestObject = request_pencari_donor.objects.all()
      data = []

      for request in requestObject:
        donor_data = Donor.objects.filter(request_id=request.pk)
        data.append({
          "donor_data": serializers.serialize("json", donor_data),
          "nama": request.nama,
          "alamat": request.alamat,
          "nomor_hp": request.nomor_hp,
          "golongan_darah": request.golongan_darah,
          "rhesus": request.rhesus,
          "pk": request.pk
        })
      requestJson = serializers.serialize("json",requestObject)
      return JsonResponse(data, safe=False)
    
    elif request.method == "POST":
      donorId = request.POST["id"]
      donor = request_pencari_donor.objects.get(pk=donorId)
      data = request_donor.objects.filter(user=request.user)
      donorObject = Donor.create(donor=request.user, donor_data= data, request = donor)
      
      donorObject.save()
      return HttpResponse("Success")

    
  return not_authenticated()

