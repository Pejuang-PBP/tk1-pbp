from django.urls import path
from .views import index, get_notifications, get_request, report, donors

urlpatterns = [
    path('', index),
    path('api/notifications', get_notifications, name="dashboard_donor_api_notifications"),
    path('api/request', get_request, name="dashboard_donor_api_notifications"),
    path('api/report', report, name="dashboard_donor_api_report"),
    path('api/donor', donors, name="dashboard_donor_api_donor"),
]

