from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Slide
from .forms import NewUserForm
from form_pencari_donor.models import request_pencari_donor
from form_donor.models import request_donor

# Create your views here.
def index(request):
  slides = Slide.objects.all().values()

  response = {
    "slides": slides, 
    "media_url": settings.MEDIA_URL
  }
  return render(request, 'index.html', response)


def signup_page(request):
  if request.user.is_authenticated:
    return redirect("home")
    
  if request.method == "POST":
    form = NewUserForm(request.POST)

    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect("home")
    else:
      return render(request, 'signup_page.html', {"form": form})

  return render(request, 'signup_page.html')


def login_page(request):
  if request.user.is_authenticated:
    return redirect("home")

  if request.method == "POST":
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get("username")
      password = form.cleaned_data.get("password")

      user = authenticate(username=username, password=password)

      if user is not None:
        login(request, user)
        return redirect("home")
    
    else:
      print(form.errors)
      return render(request, "login_page.html", {"form": form})

  return render(request, "login_page.html")


def get_count(request):
  return JsonResponse({
    "donor_count": request_donor.objects.count(),
    "recipient_count": request_pencari_donor.objects.count(),
    "user_count": User.objects.count()
  }, status=200)

def get_slides(request):
  data = []
  for slide in Slide.objects.all():
    data.append({
      "header": slide.headerText,
      "desc": slide.descText,
    })
  return JsonResponse({"data": data}, status=200)

@csrf_exempt
def test_auth(request):
  user = request.user
  print(request.POST)
  print(user)
  print(user.is_authenticated)
  if user.is_authenticated:
    return JsonResponse({"msg": "gud"})
  return JsonResponse({"msg": "bad"})