from django import forms
from data_models.models import request_donor
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
GENDER_CHOICES = [
	('Laki-Laki', 'Laki-Laki'),
	('Perempuan', 'Perempuan'),
]
BLOOD_TYPE_CHOICES = [
	('A', 'A'),
	('B', 'B'),
	('AB', 'AB'),
	('O', 'O'),
]
RHESUS_CHOICES = [
	('+', '+'),
	('-', '-'),
]
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
		

class request_donor_form(forms.ModelForm):
	tanggal_lahir = forms.DateField(validators=[age_validator], widget=forms.DateTimeInput(attrs={'type':'date','class':'form-control'}))
	
	berat_badan = forms.IntegerField(validators=[weight_validator])
	berat_badan.widget.attrs.update({'class':'form-control'})
	
	komorbid = forms.CharField(validators=[komorbid_validator], label="Apakah Anda memiliki penyakit penyerta?")
	komorbid.widget.attrs.update({'class':'form-control'})
	
	agreement = forms.BooleanField(label='Dengan ini saya menyatakan bersedia untuk menjadi pendonor plasma konvalesen', required=True)
	agreement.widget.attrs.update({'class':'form-check-input', 'type':'checkbox'})
	
	nama_lengkap = forms.CharField(label="Nama Lengkap")
	nama_lengkap.widget.attrs.update({'class':'form-control'})
	
	nik = forms.IntegerField(label='NIK')
	nik.widget.attrs.update({'class':'form-control'})
	
	no_hp = forms.CharField(label="Nomor HP")
	no_hp.widget.attrs.update({'class':'form-control'})
	
	jenis_kelamin = forms.ChoiceField(choices = GENDER_CHOICES, label="Jenis Kelamin")
	jenis_kelamin.widget.attrs.update({'class':'form-control'})
	
	tempat_lahir = forms.CharField(label="Tempat Lahir")
	tempat_lahir.widget.attrs.update({'class':'form-control'})
	
	alamat = forms.CharField(label="Alamat", widget=forms.Textarea(attrs={'class':'form-control', 'rows':3}))
	
	golongan_darah = forms.ChoiceField(choices = BLOOD_TYPE_CHOICES, label="Golongan Darah")
	golongan_darah.widget.attrs.update({'class':'form-control'})
	
	rhesus = forms.ChoiceField(choices = RHESUS_CHOICES, label="Rhesus")
	rhesus.widget.attrs.update({'class':'form-control'})
	
	tinggi_badan = forms.IntegerField(label='Tinggi Badan')
	tinggi_badan.widget.attrs.update({'class':'form-control'})
	
	class Meta:
		model = Pendonor
		#exclude = ['user']
		fields = '__all__'