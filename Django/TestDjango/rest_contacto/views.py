from django.shortcuts import render
from rest_framework import status 
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Contacto
from .serializers import ContactoSerializer
from django.core.exceptions import ObjectDoesNotExist

@csrf_exempt
@api_view(['GET','POST'])
def lista_contacto(request):
    """
    Lista todos los contacto
    """
    if request.method == 'GET':
        contacto = Contacto.objects.all()
        serializer = ContactoSerializer(contacto,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ContactoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def detalle_contacto(request, id):
    """
    get, update, o delete de contacto 
    """
    try:
        contacto = contacto.objects.get(nombre=id)
    except Contacto.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ContactoSerializer(contacto)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ContactoSerializer(contacto, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
            contacto.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.
