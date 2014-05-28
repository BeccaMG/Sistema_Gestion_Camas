from django.db import models
from app_solicitudes.models import *
from app_camas.models import *
from datetime import date

class Termometro(models.Model):

	fecha_termometro = models.DateField()
	numero = models.CharField(max_length=6, unique=True)
	fecha_ingreso = models.DateField()
