# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=100, verbose_name=b'Nombre del Banco')),
            ],
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_cuenta', models.CharField(max_length=100, verbose_name=b'Numero de cuenta', blank=True)),
                ('clabe', models.BigIntegerField(unique=True, null=True, blank=True)),
                ('tipo_cuenta', models.CharField(max_length=100, verbose_name=b'Tipo de cuenta')),
                ('monto', models.BigIntegerField(default=0)),
                ('t_tarjeta_debito', models.BooleanField(default=False)),
                ('num_tarjeta', models.CharField(max_length=100, verbose_name=b'Numero de Tarjeta de debito', blank=True)),
                ('tasa_inflacion', models.FloatField(verbose_name=b'Tasa de Inflacion')),
                ('plazo', models.IntegerField(verbose_name=b'Plazo de Inversion')),
                ('banco', models.ForeignKey(to='perfil.Banco')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Egreso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=100, verbose_name=b'Nombre del Engreso')),
                ('monto', models.FloatField(verbose_name=b'Monto')),
                ('recurrencia', models.CharField(max_length=100, verbose_name=b'recurrencia')),
                ('fijo', models.BooleanField(verbose_name=b'Es fijo')),
                ('tipo', models.CharField(max_length=100, verbose_name=b'tipo de Engreso')),
                ('fecha', models.DateField(verbose_name=b'Fecha')),
                ('financiado', models.CharField(max_length=100, verbose_name=b'Financiado')),
                ('plazo', models.IntegerField(verbose_name=b'Plazo')),
            ],
        ),
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=100, verbose_name=b'Nombre del Ingreso')),
                ('monto', models.FloatField(verbose_name=b'Monto')),
                ('recurrencia', models.CharField(max_length=100, verbose_name=b'recurrencia')),
                ('fijo', models.BooleanField(verbose_name=b'Es fijo')),
                ('tipo', models.CharField(max_length=100, verbose_name=b'tipo de ingreso')),
                ('fecha', models.DateField(verbose_name=b'Fecha')),
                ('cuenta', models.ForeignKey(to='perfil.Cuenta')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TarjetaCredito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_tarjeta', models.CharField(unique=True, max_length=100, verbose_name=b'Numero de tarjeta de credito')),
                ('limite_credito', models.FloatField(verbose_name=b'Limite de credito')),
                ('tasa_interes', models.FloatField(verbose_name=b'Tasa de interes')),
                ('alias', models.CharField(max_length=50, verbose_name=b'Alias')),
                ('fecha_corte', models.DateField(verbose_name=b'Fecha de corte')),
                ('saldo', models.FloatField(verbose_name=b'Saldo')),
                ('banco', models.ForeignKey(to='perfil.Banco')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='egreso',
            name='tarjeta',
            field=models.ForeignKey(to='perfil.TarjetaCredito'),
        ),
        migrations.AddField(
            model_name='egreso',
            name='usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
