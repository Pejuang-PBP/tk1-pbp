from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.shortcuts import render
from .models import request_pencari_donor
from form_pencari_donor.forms import request_pencari_donor_form

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
