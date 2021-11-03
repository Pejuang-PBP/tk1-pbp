from django.urls import path
from .views import index, check_question

urlpatterns = [
     path('', index, name='index'),
     path('get/ajax/check_question/', check_question, name = "check_question")
]
