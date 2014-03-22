from django import forms
from models import *
from django.forms.widgets import CheckboxSelectMultiple
from django.utils.safestring import mark_safe, SafeData

class SolicitarHabitacion(forms.Form):
    cedula = forms.IntegerField(label = "DOCUMENTO DE IDENTIDAD")
    nombres = forms.CharField(label = "NOMBRE", max_length = 64)
    apellidos = forms.CharField(label = "APELLIDO", max_length = 64)
    num_historia = forms.IntegerField(label = "NUMERO DE HISTORIA")
    fecha = forms.DateTimeField(
                label = "FECHA Y HORA DE SOLICITUD",
                widget = forms.TextInput(attrs = {'placeholder':'dd/MM/aaaa hh:mm:ss','data-format':'dd/MM/yyyy hh:mm:ss'}))
    diagnostico = forms.CharField(label = "NOMBRE MEDICO", max_length = 64)
    nombres = forms.CharField(label = "NOMBRE MEDICO", max_length = 64)
    #medico = forms.CharField()
    fecha_salida = forms.DateTimeField(
                label = "FECHA ESTIMADA DE SALIDA",
                widget = forms.TextInput(attrs = {'data-format':'dd/MM/yyyy hh:mm:ss'}))
    proveniencia = forms.ChoiceField(label = "PROVENIENCIA", choices = PROVENIENCIA)
    observacion = forms.CharField(label = "OBSERVACION", max_length = 64)
