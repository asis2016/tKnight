__author__ = 'amaharjan.de'

from rest_framework.decorators import api_view
from rest_framework.response import Response

import subprocess


@api_view(['GET'])
def get_whoami(request):
    '''
    Return `whoami` from the OS.
    '''
    result = subprocess.check_output(['whoami'], text=True).strip()
    return Response({'data': result})
