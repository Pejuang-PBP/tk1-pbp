from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PendonorForm
from django.core import serializers
from .models import Pendonor
from django.http.response import HttpResponse

"""
@login_required(login_url='/admin/login/')
def registrasi_pendonor(request):
	if not Pendonor.objects.filter(user=request.user):
		if request.method == 'POST':
			form = PendonorForm(request.POST, request.FILES)
			if form.is_valid():
				obj = form.instance
				obj.user = request.user
				obj.save()
				return JsonResponse({'msg':'Your form has been submitted successfully'})
			else:
				return JsonResponse({'msg':form.errors})
			
		else:
			return render(request, "form_donor.html", {'form': PendonorForm()})
	return render(request, "fail.html")
"""
def validasi_pendonor(obj):
	return 60 >= obj.usia >= 18 and obj.berat_badan >= 55 and not obj.gejala_covid and not obj.riwayat_transfusi and not obj.kehamilan

@login_required(login_url='/admin/login/')
def get_all_pendonor(request):
	data = serializers.serialize('json',Pendonor.objects.all())
	return HttpResponse(data, content_type="application/json")

@login_required(login_url='/admin/login')
def get_pendonor(request, id):
	data = serializers.serialize('json',Pendonor.objects.filter(id=id))
	return HttpResponse(data, content_type="application/json")