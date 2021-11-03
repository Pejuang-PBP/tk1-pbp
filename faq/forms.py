from django import forms
from django.utils.translation import gettext_lazy as _
from faq.models import Form1


class PertanyaanLain(forms.ModelForm):
    class Meta:
        model = Form1
        fields = ['name', 'pertanyaan']
        labels = {
            'name': _('Nama Lengkap'),
        }

    