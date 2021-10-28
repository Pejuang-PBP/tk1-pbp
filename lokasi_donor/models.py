from django.db import models

# Create your models here.
class UTD(models.Model):
    nama = models.CharField(max_length=50)
    kota = models.CharField(max_length=50)
    alamat = models.CharField(max_length=100)
    jamOperasi = models.CharField(max_length=50)
    nomorTelepon = models.IntegerField(default=0)
