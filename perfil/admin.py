from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Cuenta)
admin.site.register(Banco)
admin.site.register(TarjetaCredito)
admin.site.register(Ingreso)
admin.site.register(Egreso)


