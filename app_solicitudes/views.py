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

from models import *

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
			prueba = Usuario.objects.filter(cedula=u_cedula)
            prueba2 = (u_clave==u_clave0)
            if not prueba:
                if prueba2:
                    prueba2 = (u_email==u_email0)
                    if prueba2:
		              u = Usuario(username=u_cedula,cedula=u_cedula,first_name=u_nombres,habilitado=True,last_name=u_apellidos,tipo=u_tipo,administrador=u_administrador,sexo=u_sexo,tlf_cel=u_cel,direccion=u_direccion,tlf_casa=u_tlf_casa,email=u_email,password=u_clave)
		              u.is_active = True
		              u.set_password(u_clave)
		              if u_administrador == True:
		                  u.is_staff = True
		              u.save() 	
		              return redirect('/')
                    else:
		            	msj_info = "No hubo coincidencia con los emails ingresados."     
                else:
                    msj_info = "No hubo coincidencia con las claves ingresadas."     
            else:
                msj_info = "Ya hay un usuario registrado con esa cedula."     
        else:
        	msj_info = "Error con el formulario."
        msj_tipo = "error"
        info = {'msj_tipo':msj_tipo,'msj_info':msj_info,'form':form}
        return render_to_response('crearUsuario.html',info,context_instance=RequestContext(request))
    form = SolicitarHabitacion()
    info = {'form':form}
    return render_to_response('solicitarHabitacion.html',info,context_instance=RequestContext(request))