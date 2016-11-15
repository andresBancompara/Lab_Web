# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0003_auto_20161114_0439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='tasa_inflacion',
            field=models.FloatField(null=True, verbose_name=b'Tasa de Inflacion', blank=True),
        ),
    ]
