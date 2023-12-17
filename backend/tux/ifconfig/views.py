__author__ = 'amaharjan.de'

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import IfconfigSerializer

import ifcfg

@api_view(['GET'])
def get_ifconfig(request):
    '''
    Return just the default interface device dictionary.
    '''
    data = ifcfg.default_interface()
    serializer = IfconfigSerializer(data={'data':data})
    if serializer.is_valid():
        return Response(serializer.data.values())