from django.urls import path 
from rest_contacto.views import lista_contacto,detalle_contacto
urlpatterns = [
    path('lista_contacto', lista_contacto,name="lista_contacto"),
    path('detalle_contacto/<id>', detalle_contacto, name="detalle_contacto"), 
   
]
