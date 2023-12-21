__author__ = 'amaharjan.de'

from fastapi import APIRouter
import re
import subprocess

router = APIRouter()


@router.post('/ipscanner/', tags=['Networking'])
async def ip_scanner(start_ip: str, end_ip: str):
    '''
    Return a list of 'alive' IP addresses.

    :param start_ip:    The starting IP address.
    :param end_ip:      The end IP address.
    '''
    ip_alive_list = []

    # We are interested in suffix, e.g., x.x.x.1
    start_ip_suffix = '.'.join(start_ip.split('.')[3:])
    end_ip_suffix = '.'.join(end_ip.split('.')[3:])

    ip = int(start_ip_suffix)

    while ip <= int(end_ip_suffix):
        ip_address = f'{".".join(start_ip.split(".")[:3])}.{ip}'

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

    return {'result': ip_alive_list}
