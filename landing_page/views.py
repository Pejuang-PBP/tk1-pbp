from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

from .models import Slide
from .forms import NewUserForm

# Create your views here.
def index(request):
  slides = Slide.objects.all().values()

  response = {"slides": slides, "media_url": settings.MEDIA_URL}
  return render(request, 'index.html', response)


def signup_page(request):
  if request.method == "POST":
    form = NewUserForm(request.POST)
    print(form.is_valid())
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect("home")
    else:
      return render(request, 'signup_page.html', {"form": form})

  return render(request, 'signup_page.html')


def login_page(request):
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


def logout_request(request):
  logout(request)
  return redirect("home")