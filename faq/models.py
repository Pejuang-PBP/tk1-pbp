from django.db import models

# Create your models here.

class Form1(models.Model):
    
    name = models.CharField(max_length=50)
    pertanyaan = models.TextField()

class question(models.Model):
    tanya = models.CharField(max_length=100)
    jawab = models.TextField()


