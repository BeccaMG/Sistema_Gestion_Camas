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

# Cantidad de segundos en 1,2,..,6 horas
# hora_en_segundos[0] -> Segundos en 0 horas
# hora_en_segundos[1] -> Segundos en 1 hora
# .
# .
# .
# hora_en_segundos[6] -> Segundos en 6 horas
hora_en_segundos = [0,3600,7200,10800,14400,18000,21600] 

def solicitar_habitacion(request):
    mensaje = ""
    msj_tipo = ""
    msj_info = ""
    if request.method == 'POST':
        form = SolicitarHabitacion(request.POST)
        if form.is_valid():
            pcd = form.cleaned_data
            s_cedula           = pcd['cedula']
            s_nombres          = pcd['nombres']
            s_apellidos        = pcd['apellidos']
            s_num_historia     = pcd['num_historia']
            s_fecha              = pcd['fecha']
            s_diagnostico        = pcd['diagnostico']
            s_nombre_doctor      = pcd['nombre_doctor']
            s_fecha_salida       = pcd['fecha_salida']
            s_proveniencia       = pcd['proveniencia']
            s_observacion        = pcd['observacion']
            
            prueba = Paciente.objects.filter(cedula = s_cedula)
            
            if len(prueba) == 1:
                s = Solicitud(cedula = s_cedula,
                         num_historia = s_num_historia,
                         fecha = s_fecha,
                         diagnostico = s_diagnostico,
                         nombre_doctor = s_nombre_doctor,
                         fecha_salida = s_fecha_salida,
                         proveniencia = s_proveniencia,
                         observacion = s_observacion)
                s.save()
                return redirect('/emergencia/listar/todas')
            else:
                msj_tipo = "error"
                msj_info = "El paciente no se encuentra registrado en el sistema."
        info = {'msj_tipo':msj_tipo,'msj_info':msj_info,'form':form}
        return render_to_response('solicitar_habitacion.html',info,context_instance=RequestContext(request))
    form = SolicitarHabitacion()
    info = {'form':form}
    return render_to_response('solicitar_habitacion.html',info,context_instance=RequestContext(request))