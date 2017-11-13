from django.contrib import admin
from app.models import *

admin.site.register(Usuario_m) 
admin.site.register(Comentario_m)

class ImgInline(admin.StackedInline):
	model = SubirImg_m
	extra=3

class VideoInline(admin.StackedInline):
	model = SubirVideos_m
	extra=3

class DenunciaAdmin(admin.ModelAdmin):
	fieldsets=[
		('Usuario',{'fields':['user']}),
		('Informacion de Denuncia',{'fields':['titulo','descripcion']}),
		('Coordenadas',{'fields':['latitud','longitud']}),
		('Evidencia Obligatoria',{'fields':['img','video']})
		]
	inlines=[ImgInline,VideoInline]

#https://docs.djangoproject.com/es/1.11/intro/tutorial07/
admin.site.register(Denuncia_m,DenunciaAdmin)