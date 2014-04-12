from django.conf.urls import patterns, url, include

from views import *

urlpatterns = patterns('app_solicitudes.views',
    # Acesso a esperas
    url('^habitacion/solicitar$','solicitar_habitacion'),
)
