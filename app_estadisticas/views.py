from django.shortcuts import render
# Manejo de Sesion
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# General HTML
from django.shortcuts import render_to_response,redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from app_solicitudes.models import *
from app_camas.models import *
import datetime
from django.utils import timezone

from django.utils import simplejson


@login_required(login_url='/')
def termometro(request):
	camas_libres = Habitacion.objects.all().filter(estado='D')
	now = timezone.now()
	dos_dias = now - datetime.timedelta(days=2)
	camas_verde = Ingreso.objects.all().filter(habitacion__estado='O', fecha_ingreso__gte=dos_dias,fecha_ingreso__lte=now)
	
	print camas_verde
	
	return HttpResponse("hola")
	
