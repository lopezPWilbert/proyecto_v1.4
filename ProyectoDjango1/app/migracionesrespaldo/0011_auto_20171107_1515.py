# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-07 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20171107_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='denuncia_m',
            name='img',
            field=models.FileField(null=True, upload_to=b'img/%Y/%m/%d'),
        ),
    ]
