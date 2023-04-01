from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from webApi.models import Tutorial
from webApi.serializers import TutorialSerializer
from rest_framework.decorators import api_view