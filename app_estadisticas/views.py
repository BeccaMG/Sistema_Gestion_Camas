from django.shortcuts import render
# Manejo de Sesion
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# General HTML
from django.shortcuts import render_to_response,redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from app_solicitudes.models import *
from app_camas.models import *
import datetime
from django.utils import timezone
import pdb
from django.utils import simplejson

# Termometro = {'fecha':camas}
camas_prueba = Habitacion.objects.all().filter(estado='D')
camas_prueba1 = Habitacion.objects.all().filter(estado='O')
camas = [camas_prueba, camas_prueba1]
Termometro = {'2014-05-24':camas, '2014-05-25':camas}

@login_required(login_url='/')
def termometro(request):
    
    now = timezone.now()
    nowS = str(now.date())
    
    #pdb.set_trace()
    
    if (nowS > Termometro.keys()[-1]):
    
        camas_libres = Habitacion.objects.all().filter(estado='D')
        dos_dias = now - datetime.timedelta(days=2)
        cuatro_dias = now - datetime.timedelta(days=4)
        cinco_dias = now - datetime.timedelta(days=5)
        
        dos_diasS = str(dos_dias.date())
        cuatro_diasS = str(cuatro_dias.date())
        cinco_diasS = str(cinco_dias.date())
        
        camas_verdes = Ingreso.objects.all().filter(habitacion__estado='O', fecha_ingreso__gte=dos_diasS,fecha_ingreso__lte=nowS)  
        camas_amarillas = Ingreso.objects.all().filter(habitacion__estado='O', fecha_ingreso__gte=cuatro_diasS,fecha_ingreso__lte=dos_diasS)  
        camas_rojas = Ingreso.objects.all().filter(habitacion__estado='O', fecha_ingreso__lt=cuatro_diasS)  
        
        ingresos = Ingreso.objects.all()
        hoy = date.today
        
        #pdb.set_trace()
        Termometro[nowS] = [camas_libres, camas_verdes, camas_amarillas, camas_rojas]
        
        info = {
            'hoy':hoy,
            'ingresos':ingresos,
            'Termometro':Termometro,    
        }
    else:
        ingresos = Ingreso.objects.all()
        hoy = date.today
        info = {
            'Termometro':Termometro,
            'ingresos':ingresos,
            'hoy':hoy,
        }
        
    return render_to_response('estadistica_termometro.html',info,context_instance=RequestContext(request))