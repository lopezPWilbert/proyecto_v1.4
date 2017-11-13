"""
Definition of views.
"""

from django.shortcuts import render

from django.views.generic import FormView,CreateView,TemplateView, ListView,UpdateView
from django.core.urlresolvers import reverse_lazy
from .models import *
from .forms import *
from django.core import serializers
from django.http import HttpResponse
from allauth.account.views import *
from allauth.account.models import *
from allauth.socialaccount.models import SocialAccount

def DenunciaX(request):
    form2=Img_form(request.POST or None,request.FILES or None)
    form3=Video_form(request.POST or None,request.FILES or None)
    form=Denuncia_Form(request.POST or None,request.FILES or None)
    p=Denuncia_m()
    v=SubirVideos_m()
    m=SubirImg_m()
    if request.method=="POST":
        if form.is_valid() and form2.is_valid() and form3.is_valid():
            instance=form.save(commit=False)
            user = form.cleaned_data.get('user')
            titulo = form.cleaned_data.get('titulo')
            descripcion = form.cleaned_data.get('descripcion')
            latitud = form.cleaned_data.get("latitud")
            longitud = form.cleaned_data.get("longitud")

			#Datos del usuario formulario 1
            p.user=user
            p.titulo=titulo
            p.descripcion=descripcion
            p.latitud=latitud
            p.longitud=longitud
            
			#Datos del usuario formulario 2
			#imagen
            d_id = form.cleaned_data.get('id_')
            img = form.cleaned_data.get('img')
            m.d_id=d_id
            m.img=img

			#Datos del usuario formulario 3
            a_id = form.cleaned_data.get('id')
            video = form.cleaned_data.get('video')
            v.a_id=a_id
            v.video=video

            px=p.save()
            
            v.a_id=px.id
            v.save()
            m.d_id=px.pk
            m.save()

			#validacion formulario 2
            form=Denuncia_Form()
            form2=Img_form()
            form3=Video_form()
    return render(request, 'app/denuncia.html',{'form':form,'form2':form2,'form3':form3})
def Denuncia(request):
    form=Denuncia_Form(request.POST or None)
    form2=Img_form(request.POST or None)
    form3=Video_form(request.POST or None)
    #form3=Video_form(request.POST or None)
    if(request.method=='POST' and form.is_valid):
        formResult=form.save()
        if(form2.is_valid):
            formResult2=form2.save(commit=False)
            formResult2.d_id=formResult.id
            formResult2.save()
            if(form3.is_valid):
                formResult3=form3.save(commit=False)
                formResult3.a_id=formResult.id
                formResult3.save()
    return render(request, 'app/denuncia.html',{'form':form,'form2':form2, 'form3':form3})


def Denuncia_respaldp(request):
    form2=Img_form(request.POST or None,request.FILES or None)
    form3=Video_form(request.POST or None,request.FILES or None)
    form=Denuncia_Form(request.POST or None,request.FILES or None)
    if request.method=="POST":
        if form.is_valid() and form2.is_valid() and form3.is_valid():
            instance=form.save(commit=False)
            titulo = form.cleaned_data.get('titulo')
            descripcion = form.cleaned_data.get('descripcion')
            latitud = form.cleaned_data.get("latitud")
            longitud = form.cleaned_data.get("longitud")
            img = form.cleaned_data.get("img")
            video = form.cleaned_data.get("video")
			
			#validacion formulario 2
            form.save()
    return render(request, 'app/denuncia.html',{'form':form,'form2':form2,'form3':form3})

'''
class Mapa(TemplateView):
	template_name='app/mapa.html'
'''
class Mapa(ListView):
    template_name='app/mapa.html'
    model=Denuncia_m

class contador(ListView):
    template_name='app/contador.html'
    model=Denuncia_m

def Noticia(request,pk):
    ctx=Denuncia_m.objects.raw("select * from app_denuncia_m o where o.id='%s'"%(pk))
    ctx2=SubirImg_m.objects.raw("select * from app_subirimg_m o where o.d_id='%s'"%(pk))
    ctx3=SubirVideos_m.objects.raw("select * from app_subirvideos_m o where o.a_id='%s'"%(pk))
    ctx4=Comentario_m.objects.raw("select * from app_comentario_m o where o.denuncia_id='%s'"%(pk))
	
    form=Comentario_form(request.POST or None,request.FILES or None)
    if request.method == "POST":
			if form.is_valid():
				instance=form.save(commit=False)
				#user=user.id
				user = form.cleaned_data.get("user")
				denuncia = form.cleaned_data.get("denuncia")
				#denuncia=pk
				comentario = form.cleaned_data.get("comentario")
				form.save()

    return render(request,'app/noticia.html',{'ctx':ctx,'ctx2':ctx2,'ctx3':ctx3,'ctx4':ctx4,'form':form,'pk':pk})

def Perfil(request,pk):
	ctx=Comentario_m.objects.raw("select * from auth_user o where o.id='%s'"%(pk))
	ctx2=Usuario_m.objects.raw("select * from app_usuario_m o where o.nombre_id='%s'"%(pk))
	#perfil=User.socialaccount_set.all()[0].extra_data
	desicion=False		
	
	for a in ctx:
		for b in ctx2:
			if str(a.id)==str(pk) and str(b.Nombre_id)==str(pk):
				desicion=True #Actualizar
			else:
				desicion=False # Registrar

	
	return render(request,'app/perfil.html',{'ctx':ctx,'ctx2':ctx2,'pk':pk,'desicion':desicion})


#Sirve para actualizar el perfil pero ya debe de estar creado
class UpdatePerfil(UpdateView):
	template_name='app/actualizar.html'
	model=Usuario_m
	fields="__all__"


class RegisterPerfil(CreateView):
    template_name='app/registrar.html'
    model=Usuario_m
    fields='__all__'

