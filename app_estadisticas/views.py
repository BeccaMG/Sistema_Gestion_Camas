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
camas_libres = Habitacion.objects.all().filter(estado='D')
camas_verdes = []
camas_amarillas = Ingreso.objects.all().filter(habitacion__estado='O') 
camas_rojas = []
camas = [camas_libres, camas_verdes, camas_amarillas, camas_rojas]
Termometro = {'2014-06-08':camas}

# Te da la fecha del dia de la semana mas cercano hacia atras.
def dia_anterior(d, weekday):
    days_back = d.weekday() - weekday
    if days_back <= 0:
        return d
    
    return d - timedelta(days_back)

@login_required(login_url='/')
def termometro(request):
    
    total = []
   
    habs = Habitacion.objects.all().order_by('numero')

    for h in habs:
        try:
            #h1 = h.history.most_recent()
            h1 = h.history.as_of(datetime(2014, 6, 11, 13, 00, 0))
            total.append(h1)
            print "si funciono"
        except:  
            total.append(h)
            print "ocurrio una excepcion"
            
            
    #>>>> LO QUE PIENSO
    
    #Algo tipo
    #hoy = []
    #Ingreso.objects.all()
    #for i in ingreso:
        #try:
            #- pruebo si el ingreso existe para hoy a las 8:00
            #ing = i.history.as_of(hoy a las 8)
            #- si esta activo, lo meto, si no, no.
            #if activo
                #t = Termometro(fecha_termometro(hoy a las 8),
                               #numero = ing.habitacion.numero,
                               #fecha_ingreso = ing.fecha_ingreso) - no se si se crean asi los termometros XD
                #hoy.append(t)            
        #except:
            #- si no existe no importa porque capaz hay uno anterior que si pasa por el for
            
     #- despues aqui
    #habs = Habitacion.objects.all()
    #for h in habs:
        #- si existe el numero en la lista de hoy tipo:
        #if h.numero exists in hoy.termometro.numero xD:
            #- no agrego
        #else:
            #-agrego
            


   #for hab in habs:
        #try:
            #ing = Ingreso.objects.all().filter(habitacion__numero = hab)
            #print ing
            #try:
                #total[ing.habitacion.numero] = ing.como_termometro1(datetime.now())
            #except:
				#total[hab] = ing[0]
        #except:
            #total[hab] = None

   #lun = total
   #mar = []
   #mier = []
   #juev = []
   #vier = []
   #sab = []
   #dom = []
    
   #info = {
       #'lun':lun,
       #'mar':mar,
       #'mier':mier,
       #'juev':juev,
       #'vier':vier,
       #'sab':sab,
       #'dom':dom,
    #}
    
    info = {
        'habs': total,
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
