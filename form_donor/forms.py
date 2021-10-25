from django import forms
from data_models.models import Pendonor

class PendonorForm(forms.ModelForm):
	agreement = forms.BooleanField(label='Dengan ini saya menyatakan bersedia untuk menjadi pendonor plasma konvalesen', required=True)
	agreement.widget.attrs.update({'class':'form-check-input', 'type':'checkbox'})
	class Meta:
		model = Pendonor
		#exclude = ['user']
		fields = '__all__'
		widgets = {
					'nama': forms.TextInput(attrs={'class':'form-control'}),
					'no_hp': forms.NumberInput(attrs={'class':'form-control'}),
					'alamat': forms.Textarea(attrs={'class':'form-control'}),
					'jenis_kelamin': forms.Select(attrs={'class':'form-control'}),
					'kehamilan': forms.Select(attrs={'class':'form-control'}),
					'usia': forms.NumberInput(attrs={'class':'form-control'}),
					'golongan_darah': forms.Select(attrs={'class':'form-control'}),
					'rhesus': forms.Select(attrs={'class':'form-control'}),
					'berat_badan': forms.NumberInput(attrs={'class':'form-control'}),
					'gejala_covid': forms.RadioSelect(),
					'riwayat_transfusi': forms.RadioSelect(),
					'penyakit_penyerta': forms.RadioSelect(),
					'pcr_positif': forms.DateInput(attrs={'type':'date','class':'form-control'}),
					'file_pcr_positif': forms.FileInput(attrs={'type':'file', 'class':'form-control'}),
					'pcr_negatif': forms.DateInput(attrs={'type':'date','class':'form-control'}),
					'file_pcr_negatif': forms.FileInput(attrs={'type':'file', 'class':'form-control'}),
				  }