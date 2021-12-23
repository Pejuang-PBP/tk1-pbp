from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import request_donor_form
from django.core import serializers
from .models import request_donor
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime
from django.views.decorators.http import require_http_methods

@login_required(login_url='/login')
def index(request):
    if not hasattr(request.user, 'request_donor'):
        if request.method == 'POST':
            form = request_donor_form(request.POST)
            if form.is_valid():
                obj = form.instance
                obj.user = request.user
                obj.save()
                return JsonResponse({'status': 'ok', 'msg': 'Your form has been submitted successfully'})
            else:
                return JsonResponse({'status': 'error', 'msg': form.errors})

        else:
            return render(request, "form_donor.html", {'form': request_donor_form()})
    return render(request, "fail.html")

@csrf_exempt
@require_http_methods(["POST"])
def mobile(request):
	if request.user.is_authenticated and not hasattr(request.user, 'request_donor'):
		data = json.loads(request.body)
		data['tanggal_lahir'] = datetime.strptime(data['tanggal_lahir'], '%Y-%m-%d %H:%M:%S.000')
		form = request_donor_form(data);
		if form.is_valid():
			obj = form.instance
			obj.user = request.user
			obj.save();
		return JsonResponse({'status': 'ok', 'msg': 'Your form has been submitted successfully'})
	elif not request.user.is_authenticated:
		return JsonResponse({'status': 'error', 'msg': 'Silakan login terlebih dahulu'})
	else:
		return JsonResponse({'status': 'error', 'msg': 'Request sudah pernah dibuat'})