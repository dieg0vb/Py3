from django.db import models

# Create your models here.

class Articulos(models.Model):
	autor = models.CharField(max_length=30)
	titulo = models.CharField(max_length=100)
	texto = models.TextField()
	fecha = models.DateTimeField()