from django.urls import path
from .views import index, signup_page, login_page, get_count

urlpatterns = [
  path('', index, name="home"),
  path('signup', signup_page, name="signup_page"),
  path('login', login_page, name="login_page"),
  path('get_count', get_count)
]
