from django.urls import path
from .views import index, signup_page, login_page, logout_request

urlpatterns = [
  path('', index, name="home"),
  path('signup', signup_page, name="signup_page"),
  path('login', login_page, name="login_page"),
  path('logout', logout_request, name="logout")
]
