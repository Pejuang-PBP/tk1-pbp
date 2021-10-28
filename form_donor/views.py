from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import request_donor_form
from django.core import serializers
from .models import request_donor
from django.http import JsonResponse


@login_required(login_url='/login')
def index(request):
    if not hasattr(request.user, 'request_donor') and not hasattr(request.user, 'request_pencari_donor'):
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
