from django.urls import path
from form_pencari_donor.views import index, mobile

urlpatterns = [
    path('', index, name="index"),
    path('mobile', mobile, name='mobile')
]
