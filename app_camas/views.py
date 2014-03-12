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

# Create your views here.
@login_required(login_url='/')
def asignar_habitacion(request):
    habitaciones_libres = Habitacion.objects.filter(libre=True)
    titulo = "Asignacion de Habitaciones"
    info = {'habs':habitaciones_libres,
            'titulo':titulo}
    return render_to_response('asignar_habitacion.html',info,context_instance=RequestContext(request))