from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.shortcuts import render
from .models import request_pencari_donor
from form_pencari_donor.forms import request_pencari_donor_form
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime
from django.views.decorators.http import require_http_methods
# Create your views here.


@login_required(login_url='/login')
def index(request):
    if not hasattr(request.user, 'request_pencari_donor'):
        if request.method == 'POST':
            form = request_pencari_donor_form(request.POST)
            if form.is_valid():
                objek = form.instance
                objek.user = request.user
                objek.save()
                return JsonResponse({'status': 'ok', 'msg': 'Your form has been submitted succesfully'})
            else:
                return JsonResponse({'ststus': 'ok', 'msg': form.errors})
        else:
            return render(request, "form_pencari_donor.html", {'form': request_pencari_donor_form()})
    return render(request, "fail.html")

@csrf_exempt
@require_http_methods(["POST"])
def mobile(request):
    if request.user.is_authenticated and not hasattr(request.user, 'request_donor'):
        data = json.loads(request.body)
        data['tanggal_lahir'] = datetime.strptime(data['tanggal_lahir'], '%Y-%m-%d %H:%M:%S.000')
        form = request_pencari_donor_form(data);
        if form.is_valid():
            obj = form.instance
            obj.user = request.user
            obj.save();
            return JsonResponse({'status': 'ok', 'msg': 'Your form has been submitted successfully'})
        return JsonResponse({'status': 'error', 'msg': form.errors})
    elif not request.user.is_authenticated:
        return JsonResponse({'status': 'error', 'msg': 'Silakan login terlebih dahulu'})
    else:
        return JsonResponse({'status': 'error', 'msg': 'Request sudah pernah dibuat'})