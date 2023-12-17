__author__ = 'amaharjan.de'

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DiskSerializer

import psutil
import re
import json
import subprocess


@api_view(['GET'])
def disk_usage(request):
    '''
    Return disk usage statistics.
    '''
    du = psutil.disk_usage('/')
    output = dict(du._asdict())

    serializer = DiskSerializer(data={'data': output})
    if serializer.is_valid():
        return Response(serializer.data.values())


@api_view(['GET'])
def disk_partition(request):
    '''
    Return disk partition statistics.
    '''
    output = []
    data = subprocess.check_output(['df', '-h']).decode('utf-8')

    # Skip the header line
    lines = data.split('\n')[1:]

    for line in lines:
        if line.strip() == '':
            continue
        columns = re.split(r'\s+', line)
        filesystem, size, used, avail, use_percent, mounted_on = columns
        entry = {
            'Filesystem': filesystem,
            'Size': size,
            'Used': used,
            'Avail': avail,
            'Use%': use_percent,
            'Mounted on': mounted_on
        }
        output.append(entry)
    
    serializer = DiskSerializer(data={'data':output})
    if serializer.is_valid():
        return Response(serializer.data)
