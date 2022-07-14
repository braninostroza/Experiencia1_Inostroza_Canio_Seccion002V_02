from django.urls import path 
from rest_registro.views import lista_registro,detalle_registro
from rest_registro.viewslogin2 import login2
urlpatterns = [
    path('lista_registro', lista_registro,name="lista_registro"),
    path('detalle_registro/<id>', detalle_registro, name="detalle_registro"),
    path('login2', login2, name="login2"),
   
]
