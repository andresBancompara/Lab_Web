from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Banco(models.Model):
    nombre = models.CharField(verbose_name="Nombre del Banco", max_length=100, unique=True)

    def __unicode__(self):
        return self.nombre


class Cuenta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    banco = models.ForeignKey(Banco, on_delete=models.CASCADE)
    numero_cuenta = models.CharField(verbose_name="Numero de cuenta", max_length=100, blank=True)
    clabe = models.CharField(unique=True, blank=True)# maximo 18
    tipo_cuenta = models.CharField(verbose_name="Tipo de cuenta", max_length=100)
    monto = models.BigIntegerField(default=0)
    t_tarjeta_debito = models.BooleanField(default=False)
    num_tarjeta = models.CharField(verbose_name="Numero de Tarjeta de debito", max_length=100, blank=True)
    tasa_inflacion = models.FloatField(verbose_name="Tasa de Inflacion", blank=True, null=True)
    plazo = models.IntegerField(verbose_name="Plazo de Inversion", blank=True, null=True)

    def __unicode__(self):
        return self.numero_cuenta


class TarjetaCredito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    banco = models.ForeignKey(Banco, on_delete=models.CASCADE)
    numero_tarjeta = models.CharField(verbose_name="Numero de tarjeta de credito", max_length=100, unique=True)
    limite_credito = models.FloatField(verbose_name="Limite de credito")
    tasa_interes = models.FloatField(verbose_name="Tasa de interes")
    alias = models.CharField(verbose_name="Alias", max_length=50)
    fecha_corte = models.DateField(verbose_name="Fecha de corte")
    saldo = models.FloatField(verbose_name="Saldo")

    def __unicode__(self):
        return self.numero_tarjeta


class Ingreso(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    nombre = models.CharField(verbose_name="Nombre del Ingreso", max_length=100, unique=True)
    monto = models.FloatField(verbose_name="Monto")
    recurrencia = models.CharField(verbose_name="recurrencia", max_length=100)
    fijo = models.BooleanField(verbose_name="Es fijo")
    tipo = models.CharField(verbose_name="tipo de ingreso", max_length=100)
    fecha = models.DateField(verbose_name="Fecha")

    def __unicode__(self):
        return self.nombre


class Egreso(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tarjeta = models.ForeignKey(TarjetaCredito, on_delete=models.CASCADE)
    nombre = models.CharField(verbose_name="Nombre del Engreso", max_length=100, unique=True)
    monto = models.FloatField(verbose_name="Monto")
    recurrencia = models.CharField(verbose_name="recurrencia", max_length=100)
    fijo = models.BooleanField(verbose_name="Es fijo")
    tipo = models.CharField(verbose_name="tipo de Engreso", max_length=100)
    fecha = models.DateField(verbose_name="Fecha")
    financiado = models.CharField(verbose_name="Financiado", max_length=100)
    plazo = models.IntegerField(verbose_name="Plazo")

    def __unicode__(self):
        return self.nombre

