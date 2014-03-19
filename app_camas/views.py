# Manejo de Sesion
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Formularios
from django.core.context_processors import csrf
from django.template import RequestContext
from django.forms.widgets import CheckboxSelectMultiple

# General HTML
from django.shortcuts import render_to_response,redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from models import *
from app_solicitudes.models import *
from app_paciente.models import *

# Create your views here.
@login_required(login_url='/')
def asignar_habitacion(request):
	
	habitaciones_libres = Habitacion.objects.filter(libre=True)
	pacientes_quirofano = Solicitud.objects.filter(proveniencia=1)
	pacientes_emergencia_pediatra = Solicitud.objects.filter(proveniencia=2)
	pacientes_emergencia_adultos = Solicitud.objects.filter(proveniencia=3)
	pacientes_parto = Solicitud.objects.filter(proveniencia=4)
	pacientes_uci = Solicitud.objects.filter(proveniencia=5)
	pacientes_adicional = Solicitud.objects.filter(proveniencia=6)
	pacientes_especial = Solicitud.objects.filter(proveniencia=7)
	pacientes_translado = Solicitud.objects.filter(proveniencia=8)
	pacientes_otros = Solicitud.objects.filter(proveniencia=9)
	
	titulo = "Asignacion de Habitaciones"
	info = {
	'habs':habitaciones_libres,
	'pac_quirofano':pacientes_quirofano,
	'pac_emergencia_adultos':pacientes_emergencia_adultos,
	'pac_emergencia_pediatra':pacientes_emergencia_pediatra,
	'pac_parto':pacientes_parto,
	'pac_uci':pacientes_uci,
	'pac_adicional':pacientes_adicional,
	'pac_especial':pacientes_especial,
	'pac_translado':pacientes_translado,
	'pac_otros':pacientes_otros,
	'titulo':titulo}
	return render_to_response('asignar_habitacion.html',info,context_instance=RequestContext(request))