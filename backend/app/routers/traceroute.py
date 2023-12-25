__author__ = 'amaharjan.de'

from fastapi import APIRouter
import subprocess
import requests

router = APIRouter()


@router.post('/traceroute/', tags=['Networking'])
def traceroute(hostname: str):
    '''
    Traceroute endpoint that accepts a POST request with a 'hostname' parameter.
    Returns a JSON response containing traceroute information.
    '''
    API_URL = 'http://ip-api.com/json'
    
    def get_my_ip():
        '''
        Get the public IP of this system.
        '''
        response = requests.get(API_URL).json()
        return response['query']


    def get_location(ip):
        '''
        Get location details for a given IP address using the IP-API service.
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


    def run_traceroute(hostname):
        '''
        Run the 'traceroute' command and extract IP addresses from the output.
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
    
    
    my_location = get_location(get_my_ip())
    traceroute_ip_list = run_traceroute(hostname)
    geo_list = [my_location] + [get_location(ip) for ip in traceroute_ip_list if ip]
    geo_list = [loc for loc in geo_list if loc] # Filter out None values from the list
    
    return {'result': geo_list}
