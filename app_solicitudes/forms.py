from django import forms
from models import *
from django.forms.widgets import CheckboxSelectMultiple

class SolicitarHabitacion(forms.Form):
    cedula = forms.IntegerField(widget=forms.TextInput)
    num_historia = forms.IntegerField()
	fecha = forms.DateTimeField(
                label = "FECHA Y HORA DE SOLICITUD",
                widget = forms.TextInput(attrs = {'placeholder':'dd/MM/aaaa hh:mm:ss','data-format':'dd/MM/yyyy hh:mm:ss'}))
    diagnostico = forms.CharField()
	#medico = forms.CharField()
	fecha_salida = forms.DateTimeField(
                label = "FECHA ESTIMADA DE SALIDA",
                widget = forms.TextInput(attrs = {'data-format':'dd/MM/yyyy hh:mm:ss'}))
	proveniencia = forms.ChoiseField(choices = PROVENIENCIA)
	observacion = forms.CharField(max_length = 140)
