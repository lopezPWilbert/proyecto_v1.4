# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 19:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20171115_1049'),
    ]

    operations = [
        migrations.CreateModel(
            name='imagenes_m',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.FileField(blank=True, null=True, upload_to=b'img/%Y/%m/%d')),
                ('denunciaA', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Denuncia_m')),
            ],
        ),
        migrations.CreateModel(
            name='videos_m',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(blank=True, null=True, upload_to=b'img/%Y/%m/%d')),
                ('denunciaB', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Denuncia_m')),
            ],
        ),
        migrations.RemoveField(
            model_name='subirimg_m',
            name='d',
        ),
        migrations.RemoveField(
            model_name='subirvideos_m',
            name='a',
        ),
        migrations.DeleteModel(
            name='SubirImg_m',
        ),
        migrations.DeleteModel(
            name='SubirVideos_m',
        ),
    ]