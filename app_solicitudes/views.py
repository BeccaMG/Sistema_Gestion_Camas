##from django.shortcuts import render
# Manejo de Sesion
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Formularios
from django.core.context_processors import csrf
from django.template import RequestContext
from django.forms.widgets import CheckboxSelectMultiple

# General HTML
from django.shortcuts import render_to_response,redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

# Manejo de Informacion de esta aplicacion
##from forms import *
from models import *
from forms import *

# Create your views here.
def solicitar_habitacion(request):
    mensaje = ""
    if request.method == 'POST':
        form = SolicitarHabitacion(request.POST)
        if form.is_valid():
            pcd = form.cleaned_data
            u_cedula           = pcd['cedula']
            u_nombres          = pcd['nombres']
            u_apellidos        = pcd['apellidos']
            u_mun_historia     = pcd['num_historia']
        else:
        	msj_info = "Error con el formulario."
        msj_tipo = "error"
        info = {'msj_tipo':msj_tipo,'msj_info':msj_info,'form':form}
        return render_to_response('solicitar_habitacion.html',info,context_instance=RequestContext(request))
    form = SolicitarHabitacion()
    info = {'form':form}
    return render_to_response('solicitar_habitacion.html',info,context_instance=RequestContext(request))