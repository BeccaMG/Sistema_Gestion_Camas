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
from datetime import date

# Create your views here.
@login_required(login_url='/')
def asignar_habitacion(request):
	
	habitaciones_libres = Habitacion.objects.filter(libre=True)
	pacientes_quirofano = Solicitud.objects.filter(procedencia=1)
	pacientes_emergencia_pediatra = Solicitud.objects.filter(procedencia=2)
	pacientes_emergencia_adultos = Solicitud.objects.filter(procedencia=3)
	pacientes_parto = Solicitud.objects.filter(procedencia=4)
	pacientes_uci = Solicitud.objects.filter(procedencia=5)
	pacientes_adicional = Solicitud.objects.filter(procedencia=6)
	pacientes_especial = Solicitud.objects.filter(procedencia=7)
	pacientes_traslado = Solicitud.objects.filter(procedencia=8)
	pacientes_otros = Solicitud.objects.filter(procedencia=9)
	
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
	'pac_traslado':pacientes_traslado,
	'pac_otros':pacientes_otros,
	'titulo':titulo}
	return render_to_response('asignar_habitacion.html',info,context_instance=RequestContext(request))

@login_required(login_url='/')
def censo(request):
    pacientes = Ingreso.objects.all()
    hoy = date.today
    info = {
        'pacientes':pacientes,
        'hoy':hoy}
    return render_to_response('censo.html',info,context_instance=RequestContext(request))