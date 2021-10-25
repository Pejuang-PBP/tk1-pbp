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
	YES_OR_NO = [
		(True, 'Ya'),
		(False, 'Tidak'),
	]
	
	#user = models.ForeignKey(User, on_delete=models.CASCADE)
	nama = models.CharField(max_length=100)
	no_hp = models.CharField(max_length=12, verbose_name="No. Hp")
	alamat = models.TextField() 
	jenis_kelamin = models.CharField(max_length=9, choices=GENDER_CHOICES)
	kehamilan = models.BooleanField(max_length=5, choices=YES_OR_NO, verbose_name="Apakah Anda pernah atau sedang hamil?", default=False)
	usia = models.IntegerField()
	golongan_darah = models.CharField(max_length=2, choices=BLOOD_TYPE_CHOICES)
	rhesus = models.CharField(max_length=8, choices=RHESUS_CHOICES)
	berat_badan = models.IntegerField();
	gejala_covid = models.BooleanField(max_length=5, default=None, choices=YES_OR_NO, verbose_name="Apakah Anda memiliki gejala COVID-19 dalam 14 hari terakhir?")
	riwayat_transfusi = models.BooleanField(max_length=5, default=None, choices=YES_OR_NO, verbose_name="Apakah Anda memiliki riwayat transfusi darah dalam 6 bulan terakhir?")
	penyakit_penyerta = models.BooleanField(max_length=5, default=None, choices=YES_OR_NO, verbose_name="Apakah Anda memiliki penyakit penyerta (Malaria, Hipertensi, HIV, penyakit jantung, paru-paru, ginjal, dan sebagainya)?")
	positif_covid19 = models.DateField(verbose_name="Kapan pertama kali Anda dinyatakan positif COVID-19?")
	file_positif_covid19 = models.ImageField(upload_to="uploads/", verbose_name="Upload dokumen hasil pemeriksaan swab PCR positif")
	negatif_covid19 = models.DateField(verbose_name="Kapan Anda dinyatakan sembuh dari COVID-19?")
	file_negatif_covid19 = models.ImageField(upload_to="uploads/", verbose_name="Upload dokumen hasil pemeriksaan swab PCR negatif atau surat pernyataan telah sembuh minimal selama 14 hari")