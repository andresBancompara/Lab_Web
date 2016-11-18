# coding=utf-8
from django import forms
from perfil.models import *


TIPOS_CUENTA = (
    ('Cuenta de cheques', 'Cuenta de cheques'),
    ('Cuenta de ahorros', 'Cuenta de ahorros'),
    ('Certificado de depósito', 'Certificado de depósito'),
    ('Cuenta de mercado monetario', 'Cuenta de mercado monetario'),
    ('Cuentas de jubilación individual ', 'Cuentas de jubilación individual'),
)

class FormaCuenta(forms.Form):
    usuario = ??????????????????????????????????????????????????
    banco = forms.ModelChoiceField(queryset=Banco.objects.all())
    numero_cuenta = forms.CharField(label='numero_cuenta')
    clabe = forms.CharField(label='clabe', max_length=18, help_text='Clave Bancaria Estandarizada (18 numeros).')  # maximo 18
    tipo_cuenta = forms.ChoiceField(choices = TIPOS_CUENTA, label="Tipo de cuenta", initial='', widget=forms.Select(), required=True)
    monto = forms.IntegerField(label='Monto en la cuenta')
    t_tarjeta_debito = forms.BooleanField(label='Tiene tarjet de debito?')
    num_tarjeta = models.CharField(verbose_name="Numero de Tarjeta de debito", max_length=100, blank=True)
    tasa_inflacion = models.FloatField(verbose_name="Tasa de Inflacion", blank=True, null=True)
    plazo
