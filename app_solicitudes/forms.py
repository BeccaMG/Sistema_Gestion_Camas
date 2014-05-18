from django import forms
from models import *
from django.forms.widgets import CheckboxSelectMultiple
from django.utils.safestring import mark_safe, SafeData

class SolicitarHabitacion(forms.Form):
    cedula          = forms.IntegerField(widget = forms.TextInput)
    diagnostico     = forms.CharField(max_length = 64)
    cedula_doctor   = forms.IntegerField(widget = forms.TextInput)
    fecha_ingreso = forms.DateField(
                        label = "FECHA ESTIMADA DE INGRESO",
                        widget = forms.TextInput(attrs = {
                            'placeholder':'dd/MM/aaaa',
                            'data-format':'dd/MM/yyyy'
                            }))
    fecha_salida = forms.DateField(
                        label = "FECHA ESTIMADA DE SALIDA",
                        widget = forms.TextInput(attrs = {
                            'placeholder':'dd/MM/aaaa',
                            'data-format':'dd/MM/yyyy'
                            }))
    procedencia = forms.ChoiceField(choices = PROCEDENCIA)
    correo_solicitante = forms.EmailField()
    observacion = forms.CharField(max_length = 140, required = False)