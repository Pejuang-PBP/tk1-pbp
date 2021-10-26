from django import forms
from data_models.models import Pendonor
from datetime import date, datetime

"""
KOMORBID_CHOICES = [
	('Penyakit Jantung', 'Penyakit Jantung'),
	('Penyakit Hipertensi','Penyakit Hipertensi'),
	('Penyakit Paru-Paru', 'Penyakit Paru-Paru'),
	('Penyakit Hati (Liver)', 'Penyakit Hati (Liver)'),
	('Penyakit Ginjal', 'Penyakit Ginjal'),
	('Penyakit Kronik atau Neuromuskular','Penyakit Kronik atau Neuromuskular'),
	('Penyakit HIV','Penyakit HIV')
]
"""

def age_validator(val):
	curr_year = int(datetime.now().strftime("%Y"))
	diff = curr_year-val.year
	if not 60 >= diff >= 18:
		raise forms.ValidationError("Pendonor harus berusia 18-60 tahun.")
		
def weight_validator(val):
	if val < 55:
		raise forms.ValidationError("Berat badan minimal pendonor adalah 55 kg.")

def komorbid_validator(val):
	if val:
		raise forms.ValidationError("Pendonor diharuskan tidak memiliki penyakit penyerta bersifat kronis maupun penyakit yang dapat menular melalui darah.")
		

class PendonorForm(forms.ModelForm):
	agreement = forms.BooleanField(label='Dengan ini saya menyatakan bersedia untuk menjadi pendonor plasma konvalesen', required=True)
	agreement.widget.attrs.update({'class':'form-check-input', 'type':'checkbox'})
	
	tanggal_lahir = forms.DateField(validators=[age_validator], widget=forms.DateTimeInput(attrs={'type':'date','class':'form-control'}))
	
	berat_badan = forms.IntegerField(validators=[weight_validator])
	berat_badan.widget.attrs.update({'class':'form-control'})
	
	komorbid = forms.CharField(validators=[komorbid_validator], label="Apakah Anda memiliki penyakit penyerta?")
	komorbid.widget.attrs.update({'class':'form-control'})
	
	class Meta:
		model = Pendonor
		#exclude = ['user']
		fields = '__all__'
		widgets = {
					'nama_lengkap': forms.TextInput(attrs={'class':'form-control'}),
					'nik': forms.NumberInput(attrs={'class':'form-control'}),
					'no_hp': forms.NumberInput(attrs={'class':'form-control'}),
					'jenis_kelamin': forms.Select(attrs={'class':'form-control'}),
					'tempat_lahir': forms.TextInput(attrs={'class':'form-control'}),
					'alamat': forms.Textarea(attrs={'class':'form-control'}),
					'golongan_darah': forms.Select(attrs={'class':'form-control'}),
					'rhesus': forms.Select(attrs={'class':'form-control'}),
					'tinggi_badan': forms.NumberInput(attrs={'class':'form-control'}),
				  }