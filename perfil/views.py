from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import JsonResponse
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
def consultar(request, pk):
    usuario = User.objects.get(id=pk)
    cuenta = Cuenta.objects.filter(usuario=usuario)
    tarjeta = TarjetaCredito.objects.filter(usuario=usuario)
    ingresos = Ingreso.objects.filter(usuario=usuario)
    egresos = Egreso.objects.filter(usuario=usuario)

    cuentaJson = serializers.serialize("json", cuenta)
    tarjetaJson = serializers.serialize("json", tarjeta)
    ingresosJson = serializers.serialize("json", ingresos)
    egresosJson = serializers.serialize("json", egresos)

    response = '[{"Cuenta":' + cuentaJson + "}," +\
               '{"Tarjeta":' + tarjetaJson + "}," +\
               '{"Ingreso":' + ingresosJson + "}," +\
               '{"Egreso":' + egresosJson + "}]"

    return HttpResponse(response, content_type='application/json')


@token_required
def agregarCuenta(request):

    body = json.loads(request.body)

    if request.method == 'POST':
        print ("entro el post")
        username = body['username']
        user = User.objects.get(username=username)
        banco_nombre = body['banco']
        banco = Banco.objects.get(nombre=banco_nombre)
        numero_cuenta = body['numero_cuenta']
        clabe = body['clabe']
        tipo_cuenta = body['tipo_cuenta']
        monto = body['monto']
        t_tarjeta_debito = body['t_tarjeta_debito']
        num_tarjeta = body['num_tarjeta']
        tasa_inflacion = body['tasa_inflacion']
        plazo = body['plazo']

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
        data = {'Success': True}
    # if a GET (or any other method) we'll create a blank form
    else:
        print ("no entro el post")
        data = {'Success': False}

    response = JsonResponse(data)
    return response


@token_required
def modificarCuenta(request, pk):
    body = json.loads(request.body)
    data = ""
    if request.method == 'DELETE':
        cuenta = Cuenta.objects.get(pk=pk)
        cuenta.delete()
        data = {'Delete':'Eliminado'}

    if request.method == 'PUT':
        banco_nombre = body['banco']
        banco = Banco.objects.get(nombre=banco_nombre)
        numero_cuenta = body['numero_cuenta']
        clabe = body['clabe']
        tipo_cuenta = body['tipo_cuenta']
        monto = body['monto']
        t_tarjeta_debito = body['t_tarjeta_debito']
        num_tarjeta = body['num_tarjeta']
        tasa_inflacion = body['tasa_inflacion']
        plazo = body['plazo']
        try:
            cuenta = Cuenta.objects.get(id=pk)
            Cuenta.objects.filter(id=pk).update(banco=banco,
                                                numero_cuenta=numero_cuenta,
                                                clabe=clabe,
                                                tipo_cuenta=tipo_cuenta,
                                                monto=monto,
                                                t_tarjeta_debito=t_tarjeta_debito,
                                                num_tarjeta=num_tarjeta,
                                                tasa_inflacion=tasa_inflacion,
                                                plazo=plazo)

            data = {'PUT': 'Modificado'}
        except ObjectDoesNotExist:
            cuenta = None
            data = {'Error': 'Cuenta no existe'}
    else:
        data = {'Error': 'Header No existe'}
    response = JsonResponse(data)
    return response


@token_required
def consultarCuenta(request, pk):
    usuario = User.objects.get(id=pk)
    cuenta = Cuenta.objects.filter(usuario=usuario)
    response = serializers.serialize("json", cuenta)
    return HttpResponse(response, content_type='application/json')


@token_required
def agregarTarjeta(request):
    body = json.loads(request.body)
    if request.method == 'POST':
        username = body['username']
        user = User.objects.get(username=username)
        banco_nombre = body['banco']
        banco = Banco.objects.get(nombre=banco_nombre)
        numero_tarjeta = body['numero_tarjeta']
        limite_credito = body['limite_credito']
        tasa_interes = body['tasa_interes']
        alias = body['alias']
        fecha_corte = body['fecha_corte']
        saldo = body['saldo']
        tarjetaCredito = TarjetaCredito(usuario=user,
                                        banco=banco,
                                        numero_tarjeta=numero_tarjeta,
                                        limite_credito=limite_credito,
                                        tasa_interes=tasa_interes,
                                        alias=alias,
                                        fecha_corte=fecha_corte,
                                        saldo=saldo
                                        )
        tarjetaCredito.save()
        data = {'Success': True}
    else:
        print ("no entro el post")
        data = {'Success': False}

    response = JsonResponse(data)
    return response


@token_required
def modificarTarjeta(request, pk):
    body = json.loads(request.body)
    data = ""
    if request.method == 'DELETE':
        tarjeta = TarjetaCredito.objects.get(pk=pk)
        tarjeta.delete()
        data = {'Delete': 'Eliminado'}

    if request.method == 'PUT':
        banco_nombre = body['banco']
        banco = Banco.objects.get(nombre=banco_nombre)
        numero_tarjeta = body['numero_tarjeta']
        limite_credito = body['limite_credito']
        tasa_interes = body['tasa_interes']
        alias = body['alias']
        fecha_corte = body['fecha_corte']
        saldo = body['saldo']

        try:
            tarjeta = TarjetaCredito.objects.get(id=pk)
            TarjetaCredito.objects.filter(id=pk).update(banco=banco,
                                                        numero_tarjeta=numero_tarjeta,
                                                        limite_credito=limite_credito,
                                                        tasa_interes=tasa_interes,
                                                        alias=alias,
                                                        fecha_corte=fecha_corte,
                                                        saldo=saldo
                                                        )

            data = {'PUT': 'Modificado'}
        except ObjectDoesNotExist:
            tarjeta = None
            data = {'Error': 'Cuenta no existe'}
    else:
        data = {'Error': 'Header No existe'}
    response = JsonResponse(data)
    return response


@token_required
def consultarTarjeta(request, pk):
    usuario = User.objects.get(username=pk)
    tarjeta = TarjetaCredito.objects.filter(usuario=usuario)
    response = serializers.serialize("json", tarjeta)
    return HttpResponse(response, content_type='application/json')


@token_required
def agregarIngreso(request):
    body = json.loads(request.body)
    if request.method == 'POST':
        username = body['username']
        user = User.objects.get(username=username)
        cuenta = body['cuenta']
        nombre = body['nombre']
        monto = body['monto']
        recurrencia = body['recurrencia']
        fijo = body['fijo']
        tipo = body['tipo']
        fecha = body['fecha']
        ingreso = Ingreso(usuario=user,
                          cuenta=cuenta,
                          nombre=nombre,
                          monto=monto,
                          recurrencia=recurrencia,
                          fijo=fijo,
                          tipo=tipo,
                          fecha=fecha)
        ingreso.save()
        data = {'Success': True}
    else:
        print ("no entro el post")
        data = {'Success': False}

    response = JsonResponse(data)
    return response


@token_required
def modificarIngreso(request, pk):
    body = json.loads(request.body)
    data = ""
    if request.method == 'DELETE':
        ingreso = Ingreso.objects.get(pk=pk)
        ingreso.delete()
        data = {'Delete': 'Eliminado'}

    if request.method == 'PUT':
        cuenta = body['cuenta']
        nombre = body['nombre']
        monto = body['monto']
        recurrencia = body['recurrencia']
        fijo = body['fijo']
        tipo = body['tipo']
        fecha = body['fecha']

        try:
            ingreso = Ingreso.objects.get(id=pk)
            Ingreso.objects.filter(id=pk).update(cuenta=cuenta,
                                                 nombre=nombre,
                                                 monto=monto,
                                                 recurrencia=recurrencia,
                                                 fijo=fijo,
                                                 tipo=tipo,
                                                 fecha=fecha
                                                 )

            data = {'PUT': 'Modificado'}
        except ObjectDoesNotExist:
            ingreso = None
            data = {'Error': 'Cuenta no existe'}
    else:
        data = {'Error': 'Header No existe'}
    response = JsonResponse(data)
    return response


@token_required
def consultarIngreso(request, pk):
    usuario = User.objects.get(username=pk)
    ingreso = Ingreso.objects.filter(usuario=usuario)
    response = serializers.serialize("json", ingreso)
    return HttpResponse(response, content_type='application/json')


@token_required
def agregarEgreso(request):
    body = json.loads(request.body)
    if request.method == 'POST':
        username = body['username']
        user = User.objects.get(username=username)
        numero_tarjeta = body['tarjeta']
        tarjeta = TarjetaCredito.objects.get(numero_tarjeta=numero_tarjeta)
        nombre = body['nombre']
        monto = body['monto']
        recurrencia = body['recurrencia']
        fijo = body['fijo']
        tipo = body['tipo']
        fecha = body['fecha']
        financiado = body['financiado']
        plazo = body['plazo']
        egreso = Egreso(usuario=user,
                          tarjeta=tarjeta,
                          nombre=nombre,
                          monto=monto,
                          recurrencia=recurrencia,
                          fijo=fijo,
                          tipo=tipo,
                          fecha=fecha,
                          financiado=financiado,
                          plazo=plazo)
        egreso.save()
        data = {'Success': True}
    else:
        print ("no entro el post")
        data = {'Success': False}

    response = JsonResponse(data)
    return response


@token_required
def modificarEgreso(request, pk):
    body = json.loads(request.body)
    data = ""
    if request.method == 'DELETE':
        egreso = Egreso.objects.get(pk=pk)
        egreso.delete()
        data = {'Delete': 'Eliminado'}

    if request.method == 'PUT':
        numero_tarjeta = body['tarjeta']
        tarjeta = TarjetaCredito.objects.get(numero_tarjeta=numero_tarjeta)
        nombre = body['nombre']
        monto = body['monto']
        recurrencia = body['recurrencia']
        fijo = body['fijo']
        tipo = body['tipo']
        fecha = body['fecha']
        financiado = body['financiado']
        plazo = body['plazo']

        try:
            egreso = Egreso.objects.get(id=pk)
            Egreso.objects.filter(id=pk).update(tarjeta=tarjeta,
                                                nombre=nombre,
                                                monto=monto,
                                                recurrencia=recurrencia,
                                                fijo=fijo,
                                                tipo=tipo,
                                                fecha=fecha,
                                                financiado=financiado,
                                                plazo=plazo,
                                                )

            data = {'PUT': 'Modificado'}
        except ObjectDoesNotExist:
            egreso = None
            data = {'Error': 'Cuenta no existe'}
    else:
        data = {'Error': 'Header No existe'}
    response = JsonResponse(data)
    return response


@token_required
def consultarEgreso(request, pk):
    usuario = User.objects.get(username=pk)
    egreso = Egreso.objects.filter(usuario=usuario)
    response = serializers.serialize("json", egreso)
    return HttpResponse(response, content_type='application/json')


@token_required
def postPrueba(request):
    if request.method == 'POST':
        print "hola"
    print "puto"
    return HttpResponseRedirect('/convenios/')

# @login_required()
# def agregarCuenta(request):
#     username = request.session['username']
#     id_usuario = User.objects.get(username=username).id
#     user = User.objects.get(username=username)
#     if request.method == 'POST':
#         create a form instance and populate it with data from the request:
#         form = FormaCuenta(request.body)
#         check whether it's valid:
#         if form.is_valid():
#             username = form.cleaned_data['usuario']
#             #id_usuario = User.objects.get(username=username).id
#             user = User.objects.get(username=username)
#             #form.users = request.user
#             # process the data in form.cleaned_data as required
#             # usuario = form.cleaned_data
#             banco = form.cleaned_data['banco']
#             numero_cuenta = form.cleaned_data['numero_cuenta']
#             clabe = form.cleaned_data['clabe']
#             tipo_cuenta = form.cleaned_data['tipo_cuenta']
#             monto = form.cleaned_data['monto']
#             t_tarjeta_debito = form.cleaned_data['t_tarjeta_debito']
#             num_tarjeta = form.cleaned_data['num_tarjeta']
#             tasa_inflacion = form.cleaned_data['tasa_inflacion']
#             plazo = form.cleaned_data['plazo']
#             form.save(commit=False)
#             cuenta = Cuenta(usuario=user,
#                             banco=banco,
#                             numero_cuenta=numero_cuenta,
#                             clabe=clabe,
#                             tipo_cuenta=tipo_cuenta,
#                             monto=monto,
#                             t_tarjeta_debito=t_tarjeta_debito,
#                             num_tarjeta=num_tarjeta,
#                             tasa_inflacion=tasa_inflacion,
#                             plazo=plazo)
#             cuenta.save()
#             print "hola"
#             # redirect to a new URL:
#             return HttpResponseRedirect('/convenios/')
#
#
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         print ("no entro el post")
#         # form = FormaCuenta()
#         data = {'Success': False}
#
#     data = {'Success': True}
#     response = JsonResponse(data)
#     return response
