# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='plazo',
            field=models.IntegerField(verbose_name=b'Plazo de Inversion', blank=True),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='tasa_inflacion',
            field=models.FloatField(verbose_name=b'Tasa de Inflacion', blank=True),
        ),
    ]
