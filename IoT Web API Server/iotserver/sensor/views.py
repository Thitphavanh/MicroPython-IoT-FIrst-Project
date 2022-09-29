from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
import json
from .models import *


def Home(request):
    return render(request, 'sensor/home.html')

def Sensor(request):
    return render(request, 'sensor/sensor.html')

def About(request):
    return render(request, 'sensor/about.html')

def Contact(request):
    return render(request, 'sensor/contact.html')


def History(request):
    # data = TempHumid.objects.all().order_by('-id')
    data = TempHumid.objects.filter(code='TM-101').order_by('-id')
    sensor = 'Temperature sensor: #1'
    context = {'sensor': sensor, 'data': data}
    return render(request, 'sensor/history.html', context)


@api_view(['POST'])
def api_post_sensor(request):
    print('POST DATA from ESP32')

    if request.method == 'POST':
        ser = TempHumidSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
