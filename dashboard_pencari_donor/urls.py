from django.urls import path
from .views import index, get_notifications, get_request

urlpatterns = [
  path('', index),
  path('get/notifications', get_notifications),
  path('get/request', get_request)
]
