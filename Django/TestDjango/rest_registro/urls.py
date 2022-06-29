from django.urls import path 
from rest_registro.views import lista_registro,detalle_registro
urlpatterns = [
    path('lista_registro', lista_registro,name="lista_registro"),
    path('detalle_registro/<id>', detalle_registro, name="detalle_registro"), 
   
]
