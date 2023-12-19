__author__ = 'amaharjan.de'

from rest_framework.decorators import api_view
from rest_framework.response import Response

import socket


@api_view(['POST'])
def post_portscanner(request):
    '''
    Return a list of open ports of an IP address.

    Important:  
    Unauthorized port scanning can be detected and may lead to serious consequences.
    Only scan ports that you are allowed to!
    '''

    # Check if IP parameters are present in the POST request
    target_IP = request.data.get('target_IP')

    if not target_IP:
        return Response({'error': 'target_IP parameter is expected.'})

    START_PORT = 1
    END_PORT = 65535
    open_ports = []

    port = START_PORT
    while port <= END_PORT:
        print(f'Scanning port: {port}')

        # socket.AF_INET        > AF_INET stands for Address Family IPv4
        # socket.SOCK_STREAM    > connection oriented communication (TCP)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        # If result is 0, then it is successful
        result = sock.connect_ex((target_IP, port))
        if result == 0:
            open_ports.append(port)
        
        sock.close()
        port += 1
    
    return Response(
        {
            'data': open_ports,
            'totalOpenPorts': len(open_ports)
        }
    )