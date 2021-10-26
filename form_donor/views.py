from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import request_donor_form
from django.core import serializers
from .models import request_donor
from django.http.response import HttpResponse
from django.http import JsonResponse

"""
@login_required(login_url='/admin/login/')
def registrasi_pendonor(request):
	if not request_donor.objects.filter(user=request.user):
		if request.method == 'POST':
			form = request_donor_form(request.POST, request.FILES)
			if form.is_valid():
				obj = form.instance
				obj.user = request.user
				obj.save()
				return JsonResponse({'msg':'Your form has been submitted successfully'})
			else:
				return JsonResponse({'msg':form.errors})
			
		else:
			return render(request, "form_donor.html", {'form': request_donor_form()})
	return render(request, "fail.html")
"""

@login_required(login_url='/admin/login/')
def get_all_pendonor(request):
	data = serializers.serialize('json',request_donor.objects.all())
	return HttpResponse(data, content_type="application/json")

@login_required(login_url='/admin/login')
def get_pendonor(request, id):
	data = serializers.serialize('json',request_donor.objects.filter(id=id))
	return HttpResponse(data, content_type="application/json")