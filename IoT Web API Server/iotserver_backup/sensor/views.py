from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
import json

def Home(request):
	return HttpResponse('<h1>Hello World</h1>')


@api_view(['POST',])
def api_post_sensortemphumid(request):

	if request.method == 'POST':
		try:
			serializer = SensorTempHumidSerializer(data=request.data)
			print('TYPE: ',type(request.data))
			print('REQ DATA: ',request.data)

			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data,status=status.HTTP_201_CREATED)
			return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
		except:
			print('R:',request.data)
			data = json.loads(request.data)
			print(data)
			return Response(serializer.data,status=status.HTTP_201_CREATED)
