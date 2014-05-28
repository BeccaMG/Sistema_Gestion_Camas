from django.conf.urls import patterns, url, include

from views import *

urlpatterns = patterns('app_estadisticas.views',

    url('^estadisticas/termometro$','termometro'),
    url('^estadisticas/matriz$','matriz'),
   
)