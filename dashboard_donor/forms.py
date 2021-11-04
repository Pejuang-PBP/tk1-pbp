from .models import Report
from django.forms import ModelForm

class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields= ['title','message']
