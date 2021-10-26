from django.db import models

# Create your models here.
class Pendonor(models.Model):
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
	
	#user = models.ForeignKey(User, on_delete=models.CASCADE)
	nama = models.CharField(max_length=100)
	no_hp = models.CharField(max_length=12, verbose_name="No. Hp")
	alamat = models.TextField() 
	jenis_kelamin = models.CharField(max_length=9, choices=GENDER_CHOICES)
	kehamilan = models.CharField(max_length=5,default='Tidak')
	usia = models.IntegerField()
	golongan_darah = models.CharField(max_length=2, choices=BLOOD_TYPE_CHOICES)
	rhesus = models.CharField(max_length=8, choices=RHESUS_CHOICES)
	berat_badan = models.IntegerField();
	gejala_covid = models.CharField(max_length=5)
	riwayat_transfusi = models.CharField(max_length=5)
	penyakit_penyerta = models.CharField(max_length=5)
	positif_covid19 = models.DateField()
	file_positif_covid19 = models.ImageField(upload_to="uploads/", verbose_name="Upload dokumen hasil pemeriksaan swab PCR positif")
	negatif_covid19 = models.DateField()
	file_negatif_covid19 = models.ImageField(upload_to="uploads/", verbose_name="Upload dokumen hasil pemeriksaan swab PCR negatif atau surat pernyataan telah sembuh minimal selama 14 hari")