from django.urls import path
from .views import index, get_notifications

urlpatterns = [
  path('', index),
  path('get/notifications', get_notifications)
]
