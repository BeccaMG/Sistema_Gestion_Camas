from django.db import models
from app_solicitudes.models import *
from datetime import date

TIPO_HABITACION = (
    ('H','Hospitalizacion'),
    ('A','UCI-A'),
    ('P','UCI-P'),
)

ESTADO_HABITACION = (
    ('D','Disponible'),
    ('O','Ocupada'),
    ('L','En proceso de limpieza'),
    ('A','En proceso de alta'),
    ('M','En mantenimiento'),
)

class Habitacion(models.Model):
    numero    = models.CharField(max_length=6, unique=True)
    reservada = models.BooleanField(default=False)
    libre     = models.BooleanField(default=True)
    estado    = models.CharField(max_length=1, choices=ESTADO_HABITACION, 
                                 default = 'D')
    tipo      = models.CharField(max_length=1, choices=TIPO_HABITACION)
    razon     = models.CharField(max_length=140, blank = True)
    
    class Meta:
        verbose_name_plural = "Habitaciones"
        
    def __unicode__(self):
        return str(self.numero)
    
class Ingreso(models.Model):
    paciente      = models.ForeignKey(Paciente)
    solicitud     = models.ForeignKey(Solicitud)
    habitacion    = models.ForeignKey(Habitacion)
    fecha_ingreso = models.DateField(auto_now_add=True)
    alta          = models.BooleanField(default=False)
    
    def procedencia(self):
        return PROCEDENCIA[self.solicitud.procedencia - 1][1]
    
    def num_dias(self):
        today = date.today()
        dias = today - self.fecha_ingreso
        total = dias.days
        if total < 1:
            total = 1
        return total
        
    def es_hoy(self):
        today = date.today()
        if (today == self.solicitud.fecha_salida):
            return 1
        return 0