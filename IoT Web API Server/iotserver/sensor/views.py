from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
import json
import requests


def Home(request):
	return HttpResponse('<h1>Hello World</h1>')


def Table(request):
	return HttpResponse('<h1>Temp: 25 C <br>Humid: 54% </h1>')

@api_view(['POST',])
def api_post_sensor(request):
	print('POST DATA from ESP32')

	if request.method == 'POST':
		ser = TempHumidSerializer(data=request.data)
		if ser.is_valid():
			ser.save()
			return Response(ser.data, status=status.HTTP_201_CREATED)
		return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
		
		
