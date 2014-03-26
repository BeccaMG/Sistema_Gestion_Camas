from django import forms
from models import *
from django.forms.widgets import CheckboxSelectMultiple
from django.utils.safestring import mark_safe, SafeData

class SolicitarHabitacion(forms.Form):
    cedula = forms.IntegerField(widget=forms.TextInput)
    nombres = forms.CharField(max_length = 64, required = False)
    apellidos = forms.CharField(max_length = 64, required = False)
    num_historia = forms.IntegerField()
    diagnostico = forms.CharField(label = "DIAGNOSTICO", max_length = 64)
    nombre_doctor = forms.CharField(label = "NOMBRE MEDICO", max_length = 64)
    fecha_salida = forms.DateTimeField(
                label = "FECHA ESTIMADA DE SALIDA",
                widget = forms.TextInput(attrs = {'placeholder':'dd/MM/aaaa hh:mm:ss','data-format':'dd/MM/yyyy hh:mm:ss'}))
    procedencia = forms.ChoiceField(label = "PROCEDENCIA", choices = PROCEDENCIA)
    observacion = forms.CharField(label = "OBSERVACION", max_length = 140, required = False)
