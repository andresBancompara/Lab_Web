from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login', views.autenticar_usuario, name='log-in'),
    url(r'^$', views.logout, name='index')

]
