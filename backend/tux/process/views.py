__author__ = 'amaharjan.de'

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProcessSerializer

import psutil
import datetime


@api_view(['GET'])
def get_processes(request):
    '''
    Return processes of the OS.
    '''
    processes_list = []

    for proc in psutil.process_iter(['pid', 'name', 'username', 'create_time', 'terminal', 'num_threads', 'status']):
        with proc.oneshot():
            processes = {
                'pid': proc.pid,
                'process_name': proc.name(),
                'username': proc.username(),
                'created_time': datetime.datetime.fromtimestamp(proc.create_time()).strftime('%Y-%m-%d %H:%M:%S'),
                'terminal': proc.terminal(),
                'num_threads': proc.num_threads(),
                'status': proc.status(),
            }
            processes_list.append(processes)

    serializer = ProcessSerializer(data={'data':processes_list})
    if serializer.is_valid():
        return Response(serializer.data)
    

@api_view(['GET'])
def get_environ(request):
    '''
    Return all environment variables of the OS.
    '''
    env  = psutil.Process().environ()
    serializer = ProcessSerializer(data={'data':env})
    if serializer.is_valid():
        return Response(serializer.data)


