from django.conf.urls import url, include
from . import views
from perfil.views import *

urlpatterns = [

    # Pagina Principal
    url(r'^index', index),

    # Consultar
    url(r'^consultar/', consultar),

    # CRUD Cuentas
    url(r'^cuenta/', include([
        url(r'^agregar$', agregarCuenta),
        url(r'^modificar/(?P<pk>\d+)', modificarCuenta),
        url(r'^consultar/(?P<pk>\d+)', consultarCuenta),
    ])),

    # CRUD Tarjetas
    url(r'^tarjeta/', include([
        url(r'^agregar$', agregarTarjeta),
        url(r'^modificar/(?P<pk>\d+)', modificarTarjeta),
        url(r'^consultar/(?P<pk>\d+)', consultar),
    ])),

    # CRUD Ingresos
    url(r'^ingreso', include([
        url(r'^agregar$', agregarIngreso),
        url(r'^modificar/(?P<pk>\d+)', modificarIngreso),
        url(r'^consultar/(?P<pk>\d+)', consultar),
    ])),

    # CRUD Egresos
    url(r'^egreso/', include([
        url(r'^agregar$', agregarEgreso),
        url(r'^modificar/(?P<pk>\d+)', modificarEgreso),
        url(r'^consultar/(?P<pk>\d+)', consultar),
    ])),


]