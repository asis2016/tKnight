__author__ = 'amaharjan.de'

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TracerouteSerializer

import subprocess
import requests
import socket
from rest_framework import status


@api_view(['POST'])
def post_traceroute(request):
    '''
    Traceroute endpoint that accepts a POST request with a 'hostname' parameter.
    Returns a JSON response containing traceroute information.
    '''
    API_URL = 'http://ip-api.com/json'

    def run_traceroute(hostname):
        '''
        Run the 'traceroute' command and extract IP addresses from the output.

        Args:
        - hostname: Hostname to trace.

        Returns:
        - List of IP addresses.
        '''
        traceroute_process = subprocess.Popen(['traceroute', hostname], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        ip_list = []

        for line in iter(traceroute_process.stdout.readline, b''):
            line = line.decode('UTF-8')
            ips = line.split('  ')
            if len(ips) > 1:
                ip = ips[1].split('(')
                if len(ip) > 1:
                    ip = ip[1].split(')')
                    ip_list.append(ip[0])

        return ip_list

    def get_location(ip):
        '''
        Get location details for a given IP address using the IP-API service.

        Args:
        - ip: IP address.

        Returns:
        - Location details.
        '''
        response = requests.get(f'{API_URL}/{ip}')
        data = response.json()

        if data['status'] == 'success':
            return {
                'ip': data['query'],
                'lon': str(data['lon']),
                'lat': str(data['lat']),
                'city': data['city'],
                'country_code': data['countryCode'],
            }

    # Check if the 'hostname' parameter is present in the POST request
    hostname = request.data.get('hostname')
    if not hostname:
        return Response({'error': 'Hostname parameter is required in the request body.'}, status=status.HTTP_400_BAD_REQUEST)

    # Get the location details for the user's IP address
    my_location = get_location(request.META.get('REMOTE_ADDR'))

    # Trace route
    traceroute_ip_list = run_traceroute(hostname)
    geo_list = [my_location] + [get_location(ip) for ip in traceroute_ip_list if ip]

    # Filter out None values from the list
    geo_list = [loc for loc in geo_list if loc]

    serializer = TracerouteSerializer(data={'data': geo_list})
    if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Failed to serialize data.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)