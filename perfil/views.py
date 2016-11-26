
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import *
from django.forms.models import model_to_dict
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import *
from tokenapi.decorators import token_required
from tokenapi.http import JsonResponse, JsonError
import json


@login_required()
def index(request):
    monto_total = 0
    username = request.session['username']
    usuario = User.objects.get(username=username)
    cuenta = Cuenta.objects.filter(usuario=usuario)
    for c in cuenta:
        monto_total += c.monto
    print monto_total
    return render(request, 'index.html', {'monto_total': monto_total, 'usuario': usuario})
    # response = JsonResponse(model_to_dict(data))
    # return response


@token_required
def postPrueba(request):
    if request.method == 'POST':
        print "hola"
    print "puto"
    return HttpResponseRedirect('/convenios/')



@token_required
def FormularioRegistro(request):
    #username = request.session['username']

    #id_usuario = User.objects.get(username=username).id
    #user = User.objects.get(username=username)

    body=json.loads(request.body)

    if request.method == 'POST':
        print ("entro el post")
        username = body['username']
        user = User.objects.get(username=username)
        banco_nombre = body['banco']
        numero_cuenta = body['numero_cuenta']
        clabe = body['clabe']
        tipo_cuenta = body['tipo_cuenta']
        monto = body['monto']
        t_tarjeta_debito = body['t_tarjeta_debito']
        num_tarjeta = body['num_tarjeta']
        tasa_inflacion = body['tasa_inflacion']
        plazo = body['plazo']

        banco = Banco.objects.get(nombre=banco_nombre)
        cuenta = Cuenta(usuario=user,
                                banco=banco,
                                numero_cuenta=numero_cuenta,
                                clabe=clabe,
                                tipo_cuenta=tipo_cuenta,
                                monto=monto,
                                t_tarjeta_debito=t_tarjeta_debito,
                                num_tarjeta=num_tarjeta,
                                tasa_inflacion=tasa_inflacion,
                                plazo=plazo)
        cuenta.save()
        # create a form instance and populate it with data from the request:
        # form = FormaCuenta(request.body)
        # check whether it's valid:
    #     if form.is_valid():
    #         username = form.cleaned_data['usuario']
    #         #id_usuario = User.objects.get(username=username).id
    #         user = User.objects.get(username=username)
    #         #form.users = request.user
    #         # process the data in form.cleaned_data as required
    #         # usuario = form.cleaned_data
    #         banco = form.cleaned_data['banco']
    #         numero_cuenta = form.cleaned_data['numero_cuenta']
    #         clabe = form.cleaned_data['clabe']
    #         tipo_cuenta = form.cleaned_data['tipo_cuenta']
    #         monto = form.cleaned_data['monto']
    #         t_tarjeta_debito = form.cleaned_data['t_tarjeta_debito']
    #         num_tarjeta = form.cleaned_data['num_tarjeta']
    #         tasa_inflacion = form.cleaned_data['tasa_inflacion']
    #         plazo = form.cleaned_data['plazo']
    #         form.save(commit=False)
    #         cuenta = Cuenta(usuario=user,
    #                         banco=banco,
    #                         numero_cuenta=numero_cuenta,
    #                         clabe=clabe,
    #                         tipo_cuenta=tipo_cuenta,
    #                         monto=monto,
    #                         t_tarjeta_debito=t_tarjeta_debito,
    #                         num_tarjeta=num_tarjeta,
    #                         tasa_inflacion=tasa_inflacion,
    #                         plazo=plazo)
    #         cuenta.save()
    #         print "hola"
    #         # redirect to a new URL:
    #         return HttpResponseRedirect('/convenios/')
    #
    #
    # # if a GET (or any other method) we'll create a blank form
    else:
        print ("no entro el post")
        #form = FormaCuenta()
        data ={'Success': False}

    data = {'Success': True}
    response = JsonResponse(data)
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
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            cuenta = form.save()
            cuenta.save()
            return HttpResponseRedirect(self.get_success_url())
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
