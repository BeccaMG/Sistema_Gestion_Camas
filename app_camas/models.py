from django.db import models
from app_paciente.models import *
from app_usuario.models import *

# Create your models here.
class Habitacion(models.Model):
    numero = models.CharField(max_length=6, unique=True)
    libre = models.BooleanField(default=True)

    