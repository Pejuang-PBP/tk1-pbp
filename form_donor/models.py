from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class request_donor(models.Model):
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
	
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	nama = models.CharField(max_length=100)
	nomor_induk = models.CharField(max_length=16)
	nomor_hp = models.CharField(max_length=12)
	jenis_kelamin = models.CharField(max_length=9, choices=GENDER_CHOICES)
	tempat_lahir = models.CharField(max_length=100)
	tanggal_lahir = models.DateField()
	alamat = models.TextField() 
	golongan_darah = models.CharField(max_length=2, choices=BLOOD_TYPE_CHOICES)
	rhesus = models.CharField(max_length=8, choices=RHESUS_CHOICES)
	berat_badan = models.IntegerField()
	tinggi_badan = models.IntegerField()
	komorbid = models.CharField(max_length=5, choices=YES_OR_NO)