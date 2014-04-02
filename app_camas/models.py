from django.db import models
from app_paciente.models import *
from app_usuario.models import *
from datetime import datetime

# Create your models here.
class Habitacion(models.Model):
    numero =    models.CharField(max_length=6, unique=True)
    libre =     models.BooleanField(default=True)
    
class Ingreso(models.Model):
    paciente =              models.ForeignKey(Paciente)
    habitacion =            models.ForeignKey(Habitacion)
    fecha_ingreso =         models.DateTimeField(auto_now_add=True)
    fecha_estimada_salida = models.DateTimeField()
    
    def num_dias(self):
        today = datetime.today()
        print today
        dias = today - self.fecha_ingreso
        total = dias.days
        if total < 1:
            total = 1
        return total