from django.conf.urls import url, include
from . import views
from perfil.views import *

urlpatterns = [

    # Pagina Principal
    url(r'^index', index),

    # Consultar
    url(r'^consultar/', consultar),
    url(r'^consultar/bancos', consultarBanco),

    # CRUD Cuentas
    url(r'^cuenta/', include([
        url(r'^agregar$', agregarCuenta),
        url(r'^modificar/(?P<pk>\w+)', modificarCuenta),
        url(r'^consultar/(?P<pk>\w+)', consultarCuenta),
    ])),

    # CRUD Tarjetas
    url(r'^tarjeta/', include([
        url(r'^agregar$', agregarTarjeta),
        url(r'^modificar/(?P<pk>\w+)', modificarTarjeta),
        url(r'^consultar/(?P<pk>\w+)', consultarTarjeta),
    ])),

    # CRUD Ingresos
    url(r'^ingreso', include([
        url(r'^agregar$', agregarIngreso),
        url(r'^modificar/(?P<pk>\w+)', modificarIngreso),
        url(r'^consultar/(?P<pk>\w+)', consultarIngreso),
    ])),

    # CRUD Egresos
    url(r'^egreso/', include([
        url(r'^agregar$', agregarEgreso),
        url(r'^modificar/(?P<pk>\w+)', modificarEgreso),
        url(r'^consultar/(?P<pk>\w+)', consultarEgreso),
    ])),


]