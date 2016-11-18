from django.conf.urls import url
from . import views
from perfil.views import index_perfil, CuentaList, CuentaCreate, CuentaUpdate, CuentaDelete

urlpatterns = [
    url(r'^index', index_perfil),
    url(r'^listar', CuentaList.as_view(), name='cuenta_listar'),
    url(r'^nuevo', CuentaCreate.as_view(), name='cuenta_crear'),
    url(r'^editar/(?P<pk>\d+)', CuentaUpdate.as_view(), name='cuenta_editar'),
    url(r'^eliminar/(?P<pk>\d+)', CuentaDelete.as_view(), name='cuenta_eliminar'),
]