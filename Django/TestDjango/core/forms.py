from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Registro,Contacto

class RegistroForm(forms.ModelForm):

    class Meta: 
        model= Registro
        fields = ['nombre', 'correo', 'contraseña']
        labels ={
            'nombre': 'Nombre', 
            'correo': 'Correo', 
            'contraseña': 'Contraseña', 
        }
        widgets={
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nombre'
                }
            ), 
            'correo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese correo', 
                    'id': 'email'
                }
            ), 
            'contraseña': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese contraseña', 
                    'id': 'password'
                }
            )

        }

class ContactoForm(forms.ModelForm):

    class Meta: 
        model= Contacto
        fields = ['nombres', 'apellidos', 'rut', 'telefono','correo','comentario']
        labels ={
            'nombres': 'Nombres', 
            'apellidos': 'Apellidos', 
            'rut': 'Rut', 
            'telefono': 'Telefono',
            'correo': 'Correo',
            'comentario': 'Comentario',
        }
        widgets={
            'nombres': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombres', 
                    'id': 'nombre'
                }
            ), 
            'apellidos': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese apellidos', 
                    'id': 'apellidos'
                }
            ), 
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese rut', 
                    'id': 'rut'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese telefono', 
                    'id': 'fono'
                }
            ), 
            'correo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese correo', 
                    'id': 'email'
                }
            ), 
            'comentario': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese comentarios', 
                    'id': 'comentario'
                }
            )

        }
