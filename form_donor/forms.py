from django import forms
from .models import request_donor
from datetime import date, datetime
from django.core.validators import RegexValidator

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
YES_OR_NO = [
	('Ya', 'Ya'),
	('Tidak', 'Tidak'),
]

nohp_validator = RegexValidator(regex='^[0-9]*$', message="No HP hanya terdiri dari angka.")

def age_validator(val):
	curr_year = int(datetime.now().strftime("%Y"))
	diff = curr_year-val.year
	if not 60 >= diff >= 18:
		raise forms.ValidationError("Pendonor harus berusia 18-60 tahun.")
		
def weight_validator(val):
	if val < 55:
		raise forms.ValidationError("Berat badan minimal pendonor adalah 55 kg.")
		
def nik_validator(val):
	if not val.isdigit() or len(val) != 16:
		raise forms.ValidationError("NIK harus terdiri dari 16 angka")

def komorbid_validator(val):
	if val != 'Tidak':
		raise forms.ValidationError("Pendonor disyaratkan tidak memiliki penyakit penyerta bersifat kronis maupun penyakit yang dapat menular melalui darah.")
		

class request_donor_form(forms.ModelForm):
	tanggal_lahir = forms.DateField(validators=[age_validator], widget=forms.DateTimeInput(attrs={'type':'date','class':'form-control'}))
	
	berat_badan = forms.IntegerField(validators=[weight_validator])
	berat_badan.widget.attrs.update({'class':'form-control'})
	
	komorbid = forms.ChoiceField(choices = YES_OR_NO, validators=[komorbid_validator], label="Apakah Anda memiliki penyakit penyerta?", widget=forms.RadioSelect)
	
	nama = forms.CharField(label="Nama Lengkap")
	nama.widget.attrs.update({'class':'form-control'})
	
	nomor_induk = forms.CharField(validators=[nik_validator], label='NIK')
	nomor_induk.widget.attrs.update({'class':'form-control'})
	
	nomor_hp = forms.CharField(validators=[nohp_validator], label="Nomor HP")
	nomor_hp.widget.attrs.update({'class':'form-control'})
	
	jenis_kelamin = forms.ChoiceField(choices = GENDER_CHOICES, label="Jenis Kelamin")
	jenis_kelamin.widget.attrs.update({'class':'form-select'})
	
	tempat_lahir = forms.CharField(label="Tempat Lahir")
	tempat_lahir.widget.attrs.update({'class':'form-control'})
	
	alamat = forms.CharField(label="Alamat", widget=forms.Textarea(attrs={'class':'form-control', 'rows':3}))
	
	golongan_darah = forms.ChoiceField(choices = BLOOD_TYPE_CHOICES, label="Golongan Darah")
	golongan_darah.widget.attrs.update({'class':'form-select'})
	
	rhesus = forms.ChoiceField(choices = RHESUS_CHOICES, label="Rhesus")
	rhesus.widget.attrs.update({'class':'form-select'})
	
	tinggi_badan = forms.IntegerField(label='Tinggi Badan')
	tinggi_badan.widget.attrs.update({'class':'form-control'})
	
	class Meta:
		model = request_donor
		exclude = ['user']