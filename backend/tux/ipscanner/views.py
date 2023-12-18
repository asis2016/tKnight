__author__ = 'amaharjan.de'

from rest_framework.decorators import api_view
from rest_framework.response import Response

import re
import subprocess


@api_view(['POST'])
def post_ipscanner(request):
    '''
    Return a list of 'alive' IP addresses.
    '''

    # Check if IP parameters are present in the POST request
    start_IP = request.data.get('start_IP')
    end_IP = request.data.get('end_IP')

    if not start_IP or not end_IP:
        return Response({'error': 'Both start_IP and end_IP parameters are expected.'})

    
    # We are interested in suffix, e.g., x.x.x.1
    start_IP_suffix = '.'.join(start_IP.split('.')[3:])
    end_IP_suffix = '.'.join(end_IP.split('.')[3:])

    ip_alive_list = []

    ip = int(start_IP_suffix)

    while ip <= int(end_IP_suffix):
        ip_address = f"{'.'.join(start_IP.split('.')[:3])}.{ip}"

        try:
            print(f'Scanning for IP {ip_address}')
            result = subprocess.run(['ping', '-c', '1', ip_address], check=True, capture_output=True, text=True)
            
            # # Extract TTL and time values using regular expressions
            ttl_match = re.search(r'ttl=(\d+)', result.stdout)
            time_match = re.search(r'time=([\d.]+) ms', result.stdout)

            # Extract the values if matches are found
            ttl_value = ttl_match.group(1) if ttl_match else None
            time_value = time_match.group(1) if time_match else None

            result = {
                'ip': ip_address,
                'ttl': ttl_value,
                'time': time_value,
                'aliveStatus': True
            }

        except subprocess.CalledProcessError as e:
            result = {'ip': ip_address, 'aliveStatus': False}

        ip_alive_list.append(result)
        ip +=1

    return Response({'data': ip_alive_list})
    

