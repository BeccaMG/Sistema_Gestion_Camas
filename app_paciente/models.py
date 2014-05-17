# -*- encoding: utf-8 -*-

from django.db import models
from django.utils import timezone

from app_usuario.models import *


SEXO = (
    ('M','Masculino'),
    ('F','Femenino'),
)

CEDULA = (
    ('V','V'),
    ('E','E'),
)

# Create your models here.  
class Paciente(models.Model):
    num_historia                = models.IntegerField(unique = True)
    tipo_cedula                 = models.IntegerField(choices = CEDULA, max_length = 1)
    cedula                      = models.IntegerField(unique = True)
    nombres                     = models.CharField(max_length = 64)
    apellidos                   = models.CharField(max_length = 64)
    sexo                        = models.CharField(choices = SEXO, max_length = 1)
    fecha_nacimiento            = models.DateField()
    fecha_ingreso_institucion   = models.DateField()

    foto = models.ImageField(upload_to = "/static/img/pacientes/%d",default="/static/img/pacientes/person.gif")
    
    def __unicode__(self):
        return "%s, %s" % (self.apellidos,self.nombres)
