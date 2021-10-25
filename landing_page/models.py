from django.db import models

# Create your models here.
class Slide(models.Model):
    headerText = models.TextField()
    descText = models.TextField()
    bgImage = models.ImageField()