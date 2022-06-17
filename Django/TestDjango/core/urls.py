from django.urls import path
from .views import index,somos,galeria,registro,contacto,listar_registro,listar_contacto,modi_contacto,modi_registro,eli_contacto,eli_registro,aviso

urlpatterns = [
    path('', index, name="index"),
    path('somos', somos, name="somos"),
    path('galeria', galeria, name="galeria"),
    path('registro', registro, name="registro"),
    path('contacto', contacto, name="contacto"),
    path('listar_registro', listar_registro, name="listar_registro"),
    path('listar_contacto', listar_contacto, name="listar_contacto"),
    path('modi_contacto/<id>', modi_contacto, name="modi_contacto"),
    path('modi_registro/<id>', modi_registro, name='modi_registro'),
    path('eli_contacto/<id>', eli_contacto, name="eli_contacto"),
    path('eli_registro/<id>', eli_registro, name="eli_registro"),
    path('aviso', aviso, name="aviso"),
]