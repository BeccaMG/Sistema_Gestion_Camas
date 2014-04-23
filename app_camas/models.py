from django.db import models
from app_solicitudes.models import *
from datetime import datetime

ESTADO_ALTA = (
    (1,'Activo'),
    (2,'Proceso alta'),
    (3,'Alta'),
)

# Create your models here.
class Habitacion(models.Model):
    numero =    models.CharField(max_length=6, unique=True)
    libre =     models.BooleanField(default=True)
    
class Ingreso(models.Model):
    solicitud =             models.ForeignKey(Solicitud)
    habitacion =            models.ForeignKey(Habitacion)
    fecha_ingreso =         models.DateTimeField(auto_now_add=True)
   # estado      =           models.IntegerField(choices = ESTADO_ALTA, default=1)
    
    def procedencia(self):
        return PROCEDENCIA[self.solicitud.procedencia - 1][1]
    
    def num_dias(self):
        today = datetime.today()
        dias = today - self.fecha_ingreso
        total = dias.days
        if total < 1:
            total = 1
        return total

    