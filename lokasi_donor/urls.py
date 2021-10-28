from os import name
from django.urls import path
from .views import index, renderJson

urlpatterns = [
    path("", index, name="index"),
    path("/json", renderJson, name="json"),
]
