from django.urls import path
from .views import index, get_notifications, get_request

urlpatterns = [
    path('', index),
    path('api/notifications', get_notifications, name="dashboard_donor_api_notifications"),
    path('api/request', get_request, name="dashboard_donor_api_notifications"),
]
