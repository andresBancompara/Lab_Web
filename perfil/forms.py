from django import forms
from perfil.models import Cuenta, TarjetaCredito, Ingreso, Egreso


class CuentaForm(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = [
            'usuario',
            'banco',
            'numero_cuenta',
            'clabe',
            'tipo_cuenta',
            'monto',
            't_tarjeta_debito',
            'num_tarjeta',
            'tasa_inflacion',
            'plazo',
        ]
        labels = {
            'usuario': 'Usuario',
            'banco': 'Banco',
            'numero_cuenta': 'Numero de cuenta',
            'clabe': 'Clabe',
            'tipo_cuenta': 'Tipo de cuenta',
            'monto': 'Monto',
            't_tarjeta_debito': 'Tiene tarjeta de debito',
            'num_tarjeta': 'Numero de tarjeta',
            'tasa_inflacion': 'Tasa de inflacion',
            'plazo': 'Plazo',
        }