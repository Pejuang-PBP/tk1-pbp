from django.urls import path
from .views import index, include, renderJson

urlpatterns = [
    path("", index),
    path("include", include),
    path("json", renderJson, name="json"),
]
