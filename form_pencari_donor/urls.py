from django.urls import path
from form_pencari_donor.views import index

urlpatterns = [
    path('', index, name="index")
]
