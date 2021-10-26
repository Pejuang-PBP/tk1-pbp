from django.shortcuts import render
from django.conf import settings
from .models import Slide

# Create your views here.
def index(request):
  slides = Slide.objects.all().values()

  response = {"slides": slides, "media_url": settings.MEDIA_URL}
  return render(request, 'index.html', response)


def signup(request):
  return render(request, 'signup_page.html')


def login(request):
  return render(request, "login_page.html")