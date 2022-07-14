from django.shortcuts import render
from rest_framework import status 
from rest_framework.decorators import api_view,permission_classes 
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Registro 
from .serializers import RegistroSerializer
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_registro(request):
    """
    Lista todos los registro
    """
    if request.method == 'GET':
        registro = Registro.objects.all()
        serializer = RegistroSerializer(registro,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RegistroSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_registro(request, id):
    """
    get, update, o delete de un registro 
    """
    try:
        registro = Registro.objects.get(nombre=id)
    except Registro.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = RegistroSerializer(registro)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RegistroSerializer(registro, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
            registro.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.
