# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0002_auto_20161114_0437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='plazo',
            field=models.IntegerField(null=True, verbose_name=b'Plazo de Inversion', blank=True),
        ),
    ]
