from django.urls import path
from .views import index, mobile

urlpatterns = [
	path('', index, name='index'),
	path('mobile', mobile, name='mobile'),
]
