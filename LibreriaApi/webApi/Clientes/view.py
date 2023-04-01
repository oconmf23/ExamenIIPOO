from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from webApi.models import Clientes
from webApi.serializers import ClientesSerializer
from rest_framework.decorators import api_view
from django.db.utils import IntegrityError

from django.db.models import Count


from pymongo import MongoClient

from webApi.dbclasses.clientes import ClientesCollection


# Create your views here.
#@api_view(['POST'])
#def cliente_list(request):
 #   if request.method == 'POST':
  #      cliente_data = JSONParser().parse(request)
   #     cliente_serializer = ClientesSerializer(data=cliente_data)
    #    cliente = cliente.objects.filter(id_card=cliente_data['id_card'])
     #   if len(cliente) > 0:
      #      return JsonResponse({ "message": "ID already exist" }, status=status.HTTP_400_BAD_REQUEST)
        
       # if cliente_serializer.is_valid():
        #    cliente_serializer.save()
         #   return JsonResponse(cliente_serializer.data, status=status.HTTP_201_CREATED)
        #return JsonResponse(cliente_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

#@api_view(['GET', 'PUT', 'DELETE'])
#def cliente_detail(request, id):
 #   cliente = get_object_or_404(cliente, id_card=id)
  #  if request.method == 'GET':
   #     cliente_serializer = ClientesSerializer(cliente)
    #    return JsonResponse(cliente_serializer.data, safe=False)
     #   # 'safe=False' for objects serialization

    #elif request.method == 'PUT':
     #   cliente_data = JSONParser().parse(request)        
      #  cliente_serializer = ClientesSerializer(cliente, data=cliente_data)
        
       # cliente = cliente.objects.filter(id_card=cliente_data['id_card'])
        #if len(cliente) > 0 and id != cliente_data['id_card']:
         #   return JsonResponse({ "message": "ID already exist" }, status=status.HTTP_400_BAD_REQUEST)
        
        #if cliente_serializer.is_valid():
         #   cliente_serializer.save()
          #  return JsonResponse(cliente_serializer.data)
        #return JsonResponse(cliente_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #elif request.method == 'DELETE':
     #   cliente.delete()
      #  return HttpResponse(status=status.HTTP_204_NO_CONTENT)