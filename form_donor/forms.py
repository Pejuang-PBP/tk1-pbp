from django import forms
from data_models.models import Pendonor
from datetime import date

YES_OR_NO = [
	('Ya', 'Ya'),
	('Tidak', 'Tidak'),
]

def pregnancy_validator(val):
	if val != 'Tidak':
		raise forms.ValidationError("Bagi pendonor wanita disyaratkan belum pernah hamil.")

def age_validator(val):
	if not 60 >= val >= 18:
		raise forms.ValidationError("Pendonor harus berusia 18-60 tahun.")
		
def weight_validator(val):
	if val < 55:
		raise forms.ValidationError("Berat badan minimal pendonor adalah 55 kg.")

def gejala_covid_validator(val):
	if val != 'Tidak':
		raise forms.ValidationError("Pendonor harus telah sembuh dari COVID-19 (tidak memiliki gejala) minimal selama 14 hari terakhir.")
		
def riwayat_transfusi_validator(val):
	if val != 'Tidak':
		raise forms.ValidationError("Pendonor tidak boleh memiliki riwayat transfusi selama 6 bulan terakhir.")

def penyakit_penyerta_validator(val):
	if val != 'Tidak':
		raise forms.ValidationError("Pendonor diharuskan tidak memiliki penyakit penyerta bersifat kronis maupun penyakit yang dapat menular melalui darah.")
		
def date_validator(val):
	diff = date.today()-val
	if diff.days < 14:
		raise forms.ValidationError("Pendonor harus telah sembuh dari COVID-19 (tidak memiliki gejala) minimal selama 14 hari terakhir.")
		

class PendonorForm(forms.ModelForm):
	agreement = forms.BooleanField(label='Dengan ini saya menyatakan bersedia untuk menjadi pendonor plasma konvalesen', required=True)
	agreement.widget.attrs.update({'class':'form-check-input', 'type':'checkbox'})
	
	usia = forms.IntegerField(validators=[age_validator])
	usia.widget.attrs.update({'class':'form-control'})
	
	berat_badan = forms.IntegerField(validators=[weight_validator])
	berat_badan.widget.attrs.update({'class':'form-control'})
	
	kehamilan = forms.ChoiceField(choices=YES_OR_NO, validators=[pregnancy_validator])
	kehamilan.widget.attrs.update({'class':'form-control'})
	
	gejala_covid = forms.ChoiceField(validators=[gejala_covid_validator], choices=YES_OR_NO, label="Apakah Anda memiliki gejala COVID-19 dalam 14 hari terakhir?", widget=forms.RadioSelect())
	riwayat_transfusi = forms.ChoiceField(validators=[riwayat_transfusi_validator], choices=YES_OR_NO, label="Apakah Anda memiliki riwayat transfusi darah dalam 6 bulan terakhir?", widget=forms.RadioSelect())
	penyakit_penyerta = forms.ChoiceField(validators=[penyakit_penyerta_validator], choices=YES_OR_NO, label="Apakah Anda memiliki penyakit penyerta (Malaria, Hipertensi, HIV, penyakit jantung, paru-paru, ginjal, dan sebagainya)?", widget=forms.RadioSelect())
	
	positif_covid19 = forms.DateField(validators=[date_validator], label="Kapan pertama kali Anda dinyatakan positif COVID-19?", widget=forms.DateTimeInput(attrs={'type':'date','class':'form-control'}))
	negatif_covid19 = forms.DateField(validators=[date_validator], label="Kapan Anda dinyatakan sembuh dari COVID-19?", widget=forms.DateTimeInput(attrs={'type':'date','class':'form-control'}))
	class Meta:
		model = Pendonor
		#exclude = ['user']
		fields = '__all__'
		widgets = {
					'nama': forms.TextInput(attrs={'class':'form-control'}),
					'no_hp': forms.NumberInput(attrs={'class':'form-control'}),
					'alamat': forms.Textarea(attrs={'class':'form-control'}),
					'jenis_kelamin': forms.Select(attrs={'class':'form-control'}),
					'golongan_darah': forms.Select(attrs={'class':'form-control'}),
					'rhesus': forms.Select(attrs={'class':'form-control'}),
					'file_positif_covid19': forms.FileInput(attrs={'type':'file', 'class':'form-control'}),
					'file_negatif_covid19': forms.FileInput(attrs={'type':'file', 'class':'form-control'}),
				  }