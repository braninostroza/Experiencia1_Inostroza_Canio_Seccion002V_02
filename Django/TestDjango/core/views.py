from django.shortcuts import render, redirect
from .models import Registro, Contacto
from .forms import RegistroForm, ContactoForm

# Create your views here.


def index(request):

    registro= Registro.objects.all()
    contacto= Contacto.objects.all()

    datos={
        'registro': registro
    }

    datos={
        'contacto': contacto
    }

    return render(request, 'core/index.html', datos)

def contacto(request):
    if request.method=='POST': 
        contacto_form = ContactoForm(request.POST)
        if contacto_form.is_valid():
            contacto_form.save()
            return redirect('index')
    else:
        contacto_form= ContactoForm()
    return render(request, 'core/contacto.html', {'contacto_form': contacto_form})

def galeria(request):
    return render(request,'core/galeria.html')

def somos(request):
    return render(request,'core/somos.html')

def aviso(request):
    return render(request,'core/aviso-cookies.html')

def registro(request):
    if request.method=='POST': 
        registro_form = RegistroForm(request.POST)
        if registro_form.is_valid():
            registro_form.save()
            return redirect('index')
    else:
        registro_form= RegistroForm()
    return render(request, 'core/registro.html', {'registro_form': registro_form})

def listar_registro(request):
    registro= Registro.objects.all()
    datos={
        'registro': registro
    }
    return render(request,'core/listar_registro.html',datos)

def listar_contacto(request):
    contacto= Contacto.objects.all()
    datos={
        'contacto': contacto
    }
    return render(request,'core/listar_contacto.html',datos)

def modi_contacto(request, id): 
    contacto = Contacto.objects.get(id=id)
    datos = {
        'form': ContactoForm(instance=contacto)
    }
    if request.method=='POST':
        formulario = ContactoForm(data = request.POST, instance=contacto)
        if formulario.is_valid: 
            formulario.save()
            return redirect ('listar_contacto')
    return render (request, 'core/modi_contacto.html', datos ) 

def modi_registro(request, id): 
    registro = Registro.objects.get(id=id)
    datos = {
        'form': RegistroForm(instance=registro)
    }
    if request.method=='POST':
        formulario = RegistroForm(data = request.POST, instance=registro)
        if formulario.is_valid: 
            formulario.save()
            return redirect ('listar_registro')
    return render (request, 'core/modi_registro.html', datos )

def eli_contacto(request, id):
    contacto = Contacto.objects.get(id=id)
    contacto.delete()
    return redirect ('listar_contacto')

def eli_registro(request, id):
    registro = Registro.objects.get(id=id)
    registro.delete()
    return redirect ('listar_registro')          
