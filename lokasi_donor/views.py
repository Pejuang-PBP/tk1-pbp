from django.core import serializers
from django.shortcuts import render
from .models import UTD
from .filterForm import FilterKota
from django.http.response import JsonResponse

# Create your views here.
def index(request):
    utd = UTD.objects.all()
    myFilter = FilterKota(request.GET, queryset=utd)
    utd = myFilter.qs
    response = {"utd": utd, "myFilter": myFilter}
    return render(request, "lokasi_donor.html", response)


def include(request):
    return render(request, "penjelasanUTD.html")


def renderJson(request):
    data = list(UTD.objects.values())
    return JsonResponse(data, safe=False)
