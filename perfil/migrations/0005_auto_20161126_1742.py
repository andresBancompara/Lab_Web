# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-26 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0004_auto_20161114_0440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='clabe',
            field=models.CharField(blank=True, max_length=18, null=True, unique=True),
        ),
    ]