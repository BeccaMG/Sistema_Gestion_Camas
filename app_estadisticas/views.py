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
from app_estadisticas.models import *

from datetime import datetime
from django.utils import timezone
import pdb

from django.utils import simplejson
from simple_history.models import HistoricalRecords

# Termometro = {'fecha':camas}


@login_required(login_url='/')
def termometro(request):
    
    total = []
    habs = Habitacion.objects.all()
    
    for hab in habs:
        try:
            total.append(hab.como_termometro(datetime.now()))
        except:
            pass

    lun = total
    mar = []
    mier = []
    juev = []
    vier = []
    sab = []
    dom = []
    
#       camas_libres = Habitacion.objects.all().filter(estado='D')
#       dos_dias = now - datetime.timedelta(days=2)
#       cuatro_dias = now - datetime.timedelta(days=4)
#       cinco_dias = now - datetime.timedelta(days=5)
#       
#       dos_diasS = str(dos_dias.date())
#       cuatro_diasS = str(cuatro_dias.date())
#       cinco_diasS = str(cinco_dias.date())
#       
#       camas_verdes = Termometro.objects.all().filter(habitacion__estado='O', fecha_ingreso__gte=dos_diasS,fecha_ingreso__lte=nowS)  
#       camas_amarillas = Ingreso.objects.all().filter(habitacion__estado='O', fecha_ingreso__gte=cuatro_diasS,fecha_ingreso__lte=dos_diasS)  
#       camas_rojas = Ingreso.objects.all().filter(habitacion__estado='O', fecha_ingreso__lt=cuatro_diasS)  
#        
#       Termometro[nowS] = [camas_libres, camas_verdes, camas_amarillas, camas_rojas]
#

    info = {
        'lun':lun,
        'mar':mar,
        'mier':mier,
        'juev':juev,
        'vier':vier,
        'sab':sab,
        'dom':dom,
    }

    return render_to_response('estadistica_termometro.html',info,context_instance=RequestContext(request))

@login_required(login_url='/')
def matriz(request):

    hab_libre =  [ item for item in Habitacion.objects.all().filter(estado='D') ]
    hab_alta = [ item for item in Habitacion.objects.all().filter(estado='A') ]
    hab_ocu = [ item for item in Habitacion.objects.all().filter(estado='O') ]
    hab_limp = [ item for item in Habitacion.objects.all().filter(estado='L') ]
    hab_mant = [ item for item in Habitacion.objects.all().filter(estado='M') ]
    
    habs = hab_libre + hab_alta + hab_ocu + hab_limp + hab_mant
    habs.sort( key = lambda x: x.numero , reverse = False )
    info = {}
    info['habs'] = habs
    info['hoy'] = timezone.now().date()
    
    return render_to_response('estadistica_matriz.html',info,context_instance=RequestContext(request))
    