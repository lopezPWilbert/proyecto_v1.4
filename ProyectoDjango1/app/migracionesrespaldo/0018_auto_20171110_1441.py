# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-10 14:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_remove_usuario_m_correo'),
    ]

    operations = [
        migrations.AddField(
            model_name='denuncia_m',
            name='img',
            field=models.FileField(null=True, upload_to=b'img/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='denuncia_m',
            name='video',
            field=models.FileField(null=True, upload_to=b'videos/%Y/%m/%d'),
        ),
    ]
