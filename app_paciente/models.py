# -*- encoding: utf-8 -*-

from django.db import models
from django.utils import timezone

from app_usuario.models import *


SEXO = (
    ('M','Masculino'),
    ('F','Femenino'),
)

TIPO_CEDULA = (
    ('V','V'),
    ('E','E'),
)


# Create your models here.       
class Paciente(models.Model):
    num_historia                = models.IntegerField(unique = True)
    tipo_cedula                 = models.CharField(max_length = 1, 
                                                   choices = TIPO_CEDULA)
    cedula                      = models.IntegerField(unique = True)
    nombres                     = models.CharField(max_length = 64)
    apellidos                   = models.CharField(max_length = 64)
    sexo                        = models.CharField(max_length = 1, 
                                                   choices = SEXO)
    fecha_nacimiento            = models.DateField()
    fecha_ingreso_institucion   = models.DateField()
    

    foto = models.ImageField(upload_to = "/static/img/pacientes/%d",default="/static/img/pacientes/person.gif")
    
    def __unicode__(self):
        return "%s, %s" % (self.apellidos,self.nombres)

    def edad(self):
        edad = timezone.datetime.now().year - self.fecha_nacimiento.year
        mes = timezone.datetime.now().month - self.fecha_nacimiento.month
        if mes < 0:
            edad = edad -1
        elif mes == 0:
            dia = timezone.datetime.now().day - self.fecha_nacimiento.day
            if dia < 0:
                edad = edad -1
        return edad

    def meses(self):
        meses = (timezone.datetime.now().year - self.fecha_nacimiento.year)*12
        mes = timezone.datetime.now().month - self.fecha_nacimiento.month
        dia = timezone.datetime.now().day - self.fecha_nacimiento.day
        if dia < 0:
            mes = - 1
        meses = meses + mes        
        return abs(meses)