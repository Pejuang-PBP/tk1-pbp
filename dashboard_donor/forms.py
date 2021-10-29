from .models import Notifications
from django.forms import ModelForm

class NotificationsForm(ModelForm):
    class Meta:
        model = Notifications
        fields="__all__"
