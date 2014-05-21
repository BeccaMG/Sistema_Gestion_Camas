from selectable.base import ModelLookup
from selectable.registry import registry

from models import *

class MedicoLookup(ModelLookup):
    model = Medico
    search_fields = ('codigo__icontains', 
                     'first_name__icontains', 
                     'last_name__icontains',)
    
registry.register(MedicoLookup)