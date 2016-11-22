from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from .models import *
from django.forms.models import model_to_dict
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from perfil.models import Cuenta
from perfil.forms import FormaCuenta
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required

@login_required()
def index(request):
    data = Cuenta.objects.get(id=1)
    response = JsonResponse(model_to_dict(data))
    return response

class CuentaList(ListView):
    model = Cuenta
    template_name = 'cuenta_list.html'

class CuentaCreate(CreateView):
    model = Cuenta
    template_name = 'cuenta_form.html'
    form_class = FormaCuenta
    success_url = reverse_lazy('perfil:cuenta_listar')

    def get_context_data(self, **kwargs):
        context = super(CuentaCreate, self).get_context_data(**kwargs)
        if'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            cuenta = form.save()
            cuenta.save()
            return HttpResponseRedirect (self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class CuentaUpdate(UpdateView):
    model = Cuenta
    template_name = 'cuenta_form.html'
    form_class = FormaCuenta
    success_url = reverse_lazy('perfil:cuenta_listar')

    def get_context_data(self, **kwargs):
        context = super(CuentaUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        cuenta = self.model.objects.get(id=pk)
        if 'form' not in context:
            context['form'] = self.form_class()
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_cuenta = kwargs['pk']
        cuenta = self.model.objects.get(id=id_cuenta)
        form = self.form_class(request.POST, instance=cuenta)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())

class CuentaDelete(DeleteView):
    model = Cuenta
    template_name = 'cuenta_delete.html'
    success_url = reverse_lazy('perfil:cuenta_listar')

