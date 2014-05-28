from models import *
from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.
#admin.site.register(Habitacion)
admin.site.register(Ingreso)

admin.site.register(Habitacion, SimpleHistoryAdmin)