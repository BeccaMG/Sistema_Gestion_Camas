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
from django.forms.formsets import formset_factory

from models import *
from forms import *
from app_solicitudes.models import *
from datetime import date

# Create your views here.
@login_required(login_url='/')
def asignar_habitacion(request):
    
    habitaciones_libres = Habitacion.objects.filter(estado='D').order_by('numero')
    HabitacionesFormSet = formset_factory(HabitacionForm,max_num = len(habitaciones_libres))
    
    info = {}
    
    if request.method == 'POST':
        s_formset = HabitacionesFormSet(request.POST)
        
        valid_forms = False
        info['asignados'] = ''
        
        for form in s_formset:
            
            if form.is_valid():
                valid_forms = True
                
                cdata = form.cleaned_data
                
                numero_habitacion = int(cdata['numero_habitacion'])
                numero_historia = int(cdata['numero_historia'])
                nombre = str(cdata['nombre'])
                nombre_medico = str(cdata['nombre_medico'])
                fecha = cdata['fecha']
                procedencia = str(cdata['procedencia'])
                
                solicitud = Solicitud.objects.filter(num_historia=numero_historia)[0]
                hab = Habitacion.objects.filter(numero=numero_habitacion)[0]
                
                ingreso = Ingreso(
                solicitud = solicitud,
                habitacion = hab
                )
                
                ingreso.save()
                hab.estado = 'O'
                hab.save()
                solicitud.activa = False
                solicitud.save()                
                habitaciones_libres = Habitacion.objects.filter(libre=True)
            else:
                info['asignados'] = info['asignados'] + '\n' + str(form.errors)
        
        if valid_forms:
            info['asignados'] = 'Asignados los pacientes :D'
        else:
            info['error'] = 1
            
        return HttpResponseRedirect('/habitacion/asignar')
    
    pacientes_quirofano = Solicitud.objects.filter(procedencia=1, activa=True)
    pacientes_emergencia_pediatra = Solicitud.objects.filter(procedencia=2, activa=True)
    pacientes_emergencia_adultos = Solicitud.objects.filter(procedencia=3, activa=True)
    pacientes_parto = Solicitud.objects.filter(procedencia=4, activa=True)
    pacientes_uci = Solicitud.objects.filter(procedencia=5, activa=True)
    pacientes_adicional = Solicitud.objects.filter(procedencia=6, activa=True)
    pacientes_especial = Solicitud.objects.filter(procedencia=7, activa=True)
    pacientes_traslado = Solicitud.objects.filter(procedencia=8, activa=True)
    pacientes_otros = Solicitud.objects.filter(procedencia=9, activa=True)
    
    initials = []
    for libres in habitaciones_libres:
        initials.append(
        {
        'numero_habitacion': str(libres.numero),'numero_historia': '',
        'nombre': '','nombre_medico': '','fecha': '','procedencia': '',
        })
    
    formset = HabitacionesFormSet(initial=initials )
    
    titulo = "Asignacion de Habitaciones"
    info = {
    'pac_quirofano':pacientes_quirofano,
    'pac_emergencia_adultos':pacientes_emergencia_adultos,
    'pac_emergencia_pediatra':pacientes_emergencia_pediatra,
    'pac_parto':pacientes_parto,
    'pac_uci':pacientes_uci,
    'pac_adicional':pacientes_adicional,
    'pac_especial':pacientes_especial,
    'pac_traslado':pacientes_traslado,
    'pac_otros':pacientes_otros,
    'titulo':titulo,
    'formset':formset}
        
    return render_to_response('asignar_habitacion.html',info,context_instance=RequestContext(request))

def eliminar_solicitud(request):
	if request.method == 'GET':
		cedula = request.GET["cedula"]
		pac = Paciente.objects.filter(cedula = cedula)
		Solicitud.objects.filter(paciente = pac).delete()
	
	return render_to_response('censo.html',context_instance=RequestContext(request))
		
	
@login_required(login_url='/')
def censo(request):
    ingresos = Ingreso.objects.all()
    hoy = date.today
    info = {
        'ingresos':ingresos,
        'hoy':hoy,
        }
    return render_to_response('censo.html',info,context_instance=RequestContext(request))