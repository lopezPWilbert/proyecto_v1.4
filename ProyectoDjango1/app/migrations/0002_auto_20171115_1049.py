# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 18:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subirimg_m',
            old_name='img',
            new_name='imgx',
        ),
        migrations.RenameField(
            model_name='subirvideos_m',
            old_name='video',
            new_name='videox',
        ),
    ]