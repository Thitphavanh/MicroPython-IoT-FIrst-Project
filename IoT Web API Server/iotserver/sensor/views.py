from lib2to3.pgen2 import token
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
import json
from .models import *
from django.views.decorators.csrf import csrf_exempt


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


def TestShowSensor(request):
    data = TempHumid.objects.all().order_by('-id')
    sensor_list = []
    sensor_dict = {}

    for d in data:
        if d.code not in sensor_list:
            sensor_list.append(d.code)
            sensor_dict[d.code] = {'code': d.code,
                                   'title': d.title,
                                   'temperature': d.temperature,
                                   'humidity': d.humidity,
                                   'timestamp': d.timestamp.strftime('%Y-%m-%d %H:%M:%S')}

    return JsonResponse(sensor_dict, safe=True, json_dumps_params={'ensure_ascii': False})


def Sensor_list(request):
    data = TempHumid.objects.all()
    sensor_list = []
    for d in data:
        if d.code not in sensor_list:
            sensor_list.append(d.code)

    return JsonResponse(sensor_list, safe=False)


def Sensor_list_data(request):
    data = TempHumid.objects.all().order_by('-id')
    sensor_list = []
    sensor_dict = {}

    for d in data:
        if d.code not in sensor_list:
            sensor_list.append(d.code)
            sensor_dict[d.code] = {'code': d.code,
                                   'title': d.title,
                                   'temperature': d.temperature,
                                   'humidity': d.humidity,
                                   'timestamp': d.timestamp.strftime('%Y-%m-%d %H:%M:%S')}

    return JsonResponse(sensor_dict, safe=True, json_dumps_params={'ensure_ascii': False})


def Senor_current_single(request, CODE):
    data = TempHumid.objects.filter(code=CODE).order_by('-id')
    data = data[0]
    result = {'code': data.code,
              'title': data.title,
              'temperature': data.temperature,
              'humidity': data.humidity,
              'timestamp': data.timestamp.strftime('%Y-%m-%d %H:%M:%S')}
    return JsonResponse(result, safe=True, json_dumps_params={'ensure_ascii': False})


def Sensor_current_multiple(request, CODE):
    data = TempHumid.objects.filter(code=CODE).order_by('-id')
    result_list = []

    for d in data:
        result = {'code': d.code,
                  'title': d.title,
                  'temperature': d.temperature,
                  'humidity': d.humidity,
                  'timestamp': d.timestamp.strftime('%Y-%m-%d %H:%M:%S')}
        result_list.append(result)

    return JsonResponse(result_list[:10], safe=False, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
def Senor_current_multiple_post(request, CODE):
    if request.method == 'POST':
        raw_data = request.POST.copy()
        if 'token' in raw_data:
            token = raw_data.get('token')

        else:
            return JsonResponse({'status': 'no have token'}, safe=True, json_dumps_params={'ensure_ascii': False})
        token_list = ['abc123', 'xyz123']

        if token in token_list:
            data = TempHumid.objects.filter(code=CODE).order_by('-id')
            result_list = []

            for d in data:
                result = {'code': d.code,
                          'title': d.title,
                          'temperature': d.temperature,
                          'humidity': d.humidity,
                          'timestamp': d.timestamp.strftime('%Y-%m-%d %H:%M:%S')}
                result_list.append(result)

            return JsonResponse(result_list[:10], safe=True, json_dumps_params={'ensure_ascii': False})
        return JsonResponse({'status': 'invalid token error'}, safe=True, json_dumps_params={'ensure_ascii': False})

    return JsonResponse({'status': 'method error'}, safe=True, json_dumps_params={'ensure_ascii': False})
