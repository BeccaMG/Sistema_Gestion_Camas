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

# Create your views here.
@login_required(login_url='/')
def asignar_habitacion(request):
	
	habitaciones_libres = Habitacion.objects.filter(libre=True)
	pacientes_emergencia_adultos = Solicitud.objects.filter(proveniencia=3)
	
	titulo = "Asignacion de Habitaciones"
	info = {'habs':habitaciones_libres,'pac_emergencia_adultos':pacientes_emergencia_adultos,'titulo':titulo}
	return render_to_response('asignar_habitacion.html',info,context_instance=RequestContext(request))