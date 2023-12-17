__author__ = 'amaharjan.de'

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SysinfoSerializer

import psutil
import datetime


@api_view(['GET'])
def sysinfo_boottime(request):
    '''
    Return boot time info of the OS.
    '''
    bootime = psutil.boot_time()
    bootime_formatted = datetime.datetime.fromtimestamp(bootime).strftime('%Y-%m-%d %H:%M:%S')
    
    serializer = SysinfoSerializer(data={'data': bootime_formatted})
    if serializer.is_valid():
        return Response(serializer.data.values())
    

@api_view(['GET'])
def sysinfo_users(request):
    '''
    Return list of users and it's associated terminal.
    '''
    users = {}

    for user in psutil.users():
        users['name']= user[0]
        users['terminal']= user[1]
        users['host']= user[2]
        users['started']= user[3]
        users['pid']= user[4]

    serializer = SysinfoSerializer(data={'data': users})
    if serializer.is_valid():
        return Response(serializer.data.values())
