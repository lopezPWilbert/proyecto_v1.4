# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-01 00:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_denuncia2'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Denuncia',
            new_name='Denuncia_m',
        ),
        migrations.RenameModel(
            old_name='Usuario',
            new_name='Usuario_m',
        ),
    ]
