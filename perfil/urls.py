from django.conf.urls import url, include
from . import views
from perfil.views import *

urlpatterns = [

    # Pagina Principal
    url(r'^index', index),

    # CRUD Cuentas
    url(r'^cuenta', postPrueba),
    url(r'^cuenta/nueva', agregarCuenta),
    url(r'^cuenta/editar/(?P<pk>\d+)', agregarCuenta),
    url(r'^cuenta/eliminar/(?P<pk>\d+)', agregarCuenta),

    # CRUD Tarjetas
    url(r'^tarjeta', include([
        url(r'^agregar/$', agregarTarjeta),
        url(r'^modificar/$', agregarTarjeta),
        url(r'^eliminar/(?P<pk>\d+)', agregarTarjeta),
        url(r'^consultar/$', agregarTarjeta),
    ])),

    # CRUD Ingresos
    url(r'^ingreso', include([
        url(r'^agregar/$', agregarIngreso),
        url(r'^modificar/$', agregarIngreso),
        url(r'^eliminar/(?P<pk>\d+)', agregarIngreso),
        url(r'^consultar/$', agregarIngreso),
    ])),

    # CRUD Egresos
    url(r'^egreso', include([
        url(r'^agregar/$', agregarEngreso),
        url(r'^modificar/$', agregarEngreso),
        url(r'^eliminar/(?P<pk>\d+)', agregarEngreso),
        url(r'^consultar/$', agregarEngreso),
    ])),


]