__author__ = 'amaharjan.de'

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import os
import json
import psutil

from .serializers import SensorsSerializer


@api_view(['GET'])
def sensors_temperature_view(request):
    '''
    Return hardware temperatures.
    '''
    temperature = psutil.sensors_temperatures()
    serializer = SensorsSerializer(data={'data':temperature})
    if serializer.is_valid():
        return Response(serializer.data)


@api_view(['GET'])
def sensors_battery_view(request):
    '''
    Return battery information.
    '''
    battery = psutil.sensors_battery()
    battery_dict = dict(battery._asdict())
    serializer = SensorsSerializer(data={'data':battery_dict})
    if serializer.is_valid():
        return Response(serializer.data)


@api_view(['GET'])
def sensors_fans_view(request):
    '''
    Return fans information.
    '''
    fans = psutil.sensors_fans()
    serializer = SensorsSerializer(data={'data':fans})
    if serializer.is_valid():
        return Response(serializer.data.values())
