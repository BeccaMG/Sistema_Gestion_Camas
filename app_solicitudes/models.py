from django.db import models
from app_paciente.models import *
from django.utils import timezone

PROCEDENCIA = (
    (1,'Quirofano'),
    (2,'Emergencia Pediatrica'),
    (3,'Emergencia Adultos'),
    (4,'Partos'),
    (5,'UCI'),
    (6,'Adicional'),
    (7,'Especial'),
    (8,'Traslado'),
    (9,'Otros'),
)

class Solicitud(models.Model):
    paciente        = models.OneToOneField(Paciente)
    num_historia    = models.IntegerField()
    fecha           = models.DateTimeField(auto_now_add=True)
    diagnostico     = models.CharField(max_length=50)
    nombre_doctor   = models.CharField(max_length = 64)
    fecha_salida    = models.DateTimeField()
    procedencia     = models.IntegerField(choices=PROCEDENCIA)
    observacion     = models.CharField(max_length=140)
    