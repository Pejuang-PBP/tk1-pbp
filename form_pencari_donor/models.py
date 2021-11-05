from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class request_pencari_donor(models.Model):
    ROLE_GENDER = [
        ('Laki-laki', 'LAKI-LAKI'),
        ('Perempuan', 'PEREMPUAN')
    ]
    RHESUS = [
		('+', '+'),
		('-', '-'),
	]
    BLOOD_TYPE_CHOICES = [
		('A', 'A'),
		('B', 'B'),
		('AB', 'AB'),
		('O', 'O'),
	]
    URGENCY = [
        ('LOW', 'LOW'),
        ('MEDIUM', 'MEDIUM'),
        ('HIGH', 'HIGH')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=100)
    nomor_induk = models.CharField(max_length=16)
    nomor_hp = models.CharField(max_length=12)
    jenis_kelamin = models.CharField(max_length=10, choices=ROLE_GENDER)
    tempat_lahir = models.CharField(max_length=10)
    tanggal_lahir = models.DateField()
    alamat = models.TextField()
    golongan_darah = models.CharField(max_length=2, choices=BLOOD_TYPE_CHOICES)
    rhesus = models.CharField(max_length=8, choices=RHESUS)
    tempat_rawat = models.TextField()
    urgency = models.CharField(max_length=10, choices=URGENCY)