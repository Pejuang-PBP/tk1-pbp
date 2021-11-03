from django.shortcuts import render
from .models import UTD
from .filterForm import FilterKota

# Create your views here.
def index(request):
    utd = UTD.objects.all()
    myFilter = FilterKota(request.GET, queryset=utd)
    utd = myFilter.qs
    response = {"utd": utd, "myFilter": myFilter}
    return render(request, "lokasi_donor.html", response)


def include(request):
    return render(request, "penjelasanUTD.html")
