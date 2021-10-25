from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'index_pencari_donor.html')