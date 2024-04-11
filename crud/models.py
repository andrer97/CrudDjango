from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    dataNascimento = models.DateField()
    email = models.CharField(max_length=50)
    paisDestino = models.CharField(max_length=50)
