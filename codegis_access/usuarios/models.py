'''
    Modelo(s) encargados de administrar los usuarios y los campos
    que se extienden al modelo User de Django
'''

from django.db import models
from django.contrib.auth.models import User

# definicion de campos para extender modelo User de Django
TELEFONO  = models.CharField(max_length = 20 ,blank          = True, verbose_name     = 'Teléfono', help_text       = 'Teléfono del usuario')
IDENTIDAD = models.CharField(max_length = 13, null           = True, verbose_name     = 'Identificación', help_text = 'Identificación del usuario')
DIRECCION = models.TextField(blank      = True, verbose_name = 'Direccion', help_text = 'Direccion del usuario')

# extender model User de Django con los campos definidos
TELEFONO.contribute_to_class(User, 'telefono')
IDENTIDAD.contribute_to_class(User, 'identidad')
DIRECCION.contribute_to_class(User, 'direccion')
