from django import forms
from models import *
from app_usuario.lookups import MedicoLookup

from selectable.forms import AutoCompleteWidget

class SolicitarHabitacion(forms.Form):
    cedula          = forms.IntegerField(widget = forms.TextInput)
    diagnostico     = forms.CharField(max_length = 64)
    #cedula_doctor   = forms.IntegerField(widget = forms.TextInput)
    cedula_doctor   = forms.CharField(
                        label='Type the name of a fruit (AutoCompleteWidget)',
                        widget = AutoCompleteWidget(MedicoLookup),
                        required=False,
    )
    fecha_ingreso = forms.DateField(
                        label = "FECHA ESTIMADA DE INGRESO",
                        widget = forms.TextInput(attrs = {
                            'placeholder':'dd/mm/aaaa',
                            'data-format':'dd/mm/yyyy'
                            }))
    fecha_salida = forms.DateField(
                        label = "FECHA ESTIMADA DE SALIDA",
                        widget = forms.TextInput(attrs = {
                            'placeholder':'dd/mm/aaaa',
                            'data-format':'dd/mm/yyyy'
                            }))
    procedencia = forms.ChoiceField(choices = PROCEDENCIA)
    correo_solicitante = forms.EmailField()
    observacion = forms.CharField(max_length = 140, required = False)