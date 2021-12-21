import json
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from landing_page.forms import NewUserForm

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Redirect to a success page.
            return JsonResponse({
              "status": True,
              "username": user.username,
              "message": "Successfully Logged In!"
            })
        else:
            return JsonResponse({
              "status": False,
              "message": "Failed to Login, Account Disabled."
            }, status=401)
            
    else:
        return JsonResponse({
          "status": False,
          "message": "Failed to Login, check your email/password."
        }, status=401)


@csrf_exempt
def signup(request):
  form = NewUserForm(json.loads(request.body))
  if form.is_valid():
    user = form.save()
    auth_login(request, user)
    return JsonResponse({
      "status": True,
      "message": "Signup successful",
    }, status=200)
  else:
    return JsonResponse(form.errors, status=400)