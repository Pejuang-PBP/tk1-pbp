from django.urls import path
from .views import *

urlpatterns = [
  path('', index, name="home"),
  path('signup', signup_page, name="signup_page"),
  path('login', login_page, name="login_page"),
  path('api/counts', get_count, name="get_count"),
  path('api/slides', get_slides, name="get_slides"),
  path('test', test_auth)
]
