from django.conf.urls import patterns, include, url
from AM import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    ## APLICACIONES PROPIAS
    # Atencion
    url(r'^', include('app_camas.urls')),
	url(r'^', include('app_solicitudes.urls')),
	
    # Usuario
    url('^$','app_usuario.views.sesion_iniciar'),
    url('^sesion/iniciar/$','app_usuario.views.sesion_iniciar'),
    url('^sesion/cerrar$','app_usuario.views.sesion_cerrar'),
    url('^usuario/solicitar$','app_usuario.views.usuario_solicitar'),
    url('^usuario/pendientes$','app_usuario.views.usario_listarPendientes'),
    url('^usuario/listar$','app_usuario.views.usario_listar'),
    url('^usuario/pendientes/(?P<cedulaU>\d+)/aprobar$',
        'app_usuario.views.usuario_aprobar'),
    url('^usuario/pendientes/(?P<cedulaU>\d+)/rechazar$',
        'app_usuario.views.usuario_rechazar'),
    url('^usuario/pendientes/(?P<cedulaU>\d+)/examinar$',
        'app_usuario.views.pendiente_examinar'),
    url('^usuario/clave$','app_usuario.views.clave_cambiar'),
    url('^usuario/restablecer$','app_usuario.views.clave_restablecer'),
    url('^usuario/crear$','app_usuario.views.usuario_crear'),
    url('^usuario/listar/(?P<cedulaU>\d+)/habilitar$',
        'app_usuario.views.usuario_habilitar'),
    url('^usuario/listar/(?P<cedulaU>\d+)/deshabilitar$',
        'app_usuario.views.usuario_deshabilitar'),
    url('^usuario/listar/(?P<cedulaU>\d+)/examinar$',
        'app_usuario.views.usuario_examinar'),
    

    ## COSAS DJANGISTICAS
    # Admin
    url(r'^admin/', include(admin.site.urls)),
    # Media
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    # Static
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT}),


    # Examples:
    # url(r'^$', 'AM.views.home', name='home'),
    # url(r'^AM/', include('AM.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
