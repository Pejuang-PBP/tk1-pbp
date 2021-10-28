from django.shortcuts import render
from .models import UTD
from django.http.response import HttpResponse
from django.core import serializers
from .filterForm import FilterKota

# Create your views here.
def index(request):
    utd = UTD.objects.all()
    myFilter = FilterKota(request.GET, queryset=utd)
    utd = myFilter.qs
    response = {"utd": utd, "myFilter": myFilter}
    return render(request, "lokasi_donor.html", response)


def renderJson(request):
    data = serializers.serialize("json", UTD.objects.all())
    return HttpResponse(data, content_type="application/json")
