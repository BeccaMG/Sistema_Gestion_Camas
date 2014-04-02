from django.db import models
from django.contrib.auth.models import User

SEXO = (
    ('1','Masculino'),
    ('2','Femenino'),
)

USUARIO = (
    ('A','Administracion'),
    ('R','Responsable'),
    ('M','Medico'),
    ('L','Limpieza'),
    ('S','Solicitante'),
)

# Create your models here.
class Usuario(User):
    cedula        = models.IntegerField(default=0, unique=True)
    tipo          = models.CharField(max_length=1,choices=USUARIO)
    administrador = models.BooleanField(default=False)
    sexo          = models.CharField(max_length=1,choices=SEXO)
    tlf_cel       = models.CharField(max_length=11) 	
    direccion     = models.CharField(max_length=128)
    tlf_casa      = models.CharField(max_length=11)
    habilitado    = models.BooleanField(default=False)

    def sexoR(self):
        resp = "Hombre"
        if (self.sexo == '2'):
            resp = "Mujer"
        return resp

    def tipoR(self):
        resp = "Administracion"
        if (self.tipo == 'R'):
            resp = "Responsable"
        if (self.tipo == 'M'):
            resp = "Medico"
        if (self.tipo == 'L'):
            resp = "Limpieza"
        if (self.tipo == 'S'):
            resp = "Solicitante"
        return resp
    
    def is_admin(self):
        return (self.tipo == 'A')
    def is_medico(self):
        return (self.tipo == 'M')
    def is_limpieza(self):
        return (self.tipo == 'L')
    def is_sol(self):
        return (self.tipo == 'S')
    def is_resp(self):
        return (self.tipo == 'R')
    

class Medico(Usuario):
    especialidad = models.CharField(max_length=128)