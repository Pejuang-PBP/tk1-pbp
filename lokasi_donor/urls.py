from django.urls import path
from .views import index, include

urlpatterns = [
    path("", index),
    path("include", include),
]
