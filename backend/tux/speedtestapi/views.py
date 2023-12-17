__author__ = 'amaharjan.de'

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SpeedtestapiSerializer

import subprocess


@api_view(['GET'])
def get_speedtest(request):
    '''
    Return internet speed test, i.e., upload, download and ping time taken.
    '''
    bytes_data = subprocess.check_output(['speedtest-cli', '--simple'])
    string_data = bytes_data.decode('utf-8')
    lines = string_data.split('\n')

    result = {}

    for line in lines:
        if line.strip():  # Ignore empty lines
            key, value = line.split(': ')
            result[key.lower()] = value

    serializer = SpeedtestapiSerializer(data={'data':result})
    if serializer.is_valid():
        return Response(serializer.data.values())

