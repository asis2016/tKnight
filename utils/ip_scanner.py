"""
Utility function to retrieve Return a list of 'alive' IP addresses.
"""

__author__ = "Ashish S. Maharjan"
__email__ = "hello@amaharjan.de"
__version__ = "1.0"

import re
import subprocess
import concurrent.futures

def get_ips(start_ip: str, end_ip: str):
    try:
        start_ip_suffix = '.'.join(start_ip.split('.')[3:])
        end_ip_suffix = '.'.join(end_ip.split('.')[3:])
        ip_alive_list = []

        def scan_ip(ip_address):
            try:
                print(f'Scanning for IP {ip_address}')
                result = subprocess.run(['ping', '-c', '1', ip_address], check=True, capture_output=True, text=True)
                
                ttl_match = re.search(r'ttl=(\d+)', result.stdout)
                time_match = re.search(r'time=([\d.]+) ms', result.stdout)

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

            return result

        def worker(ip_address):
            result = scan_ip(ip_address)
            ip_alive_list.append(result)

        with concurrent.futures.ThreadPoolExecutor() as executor:
            ip = int(start_ip_suffix)
            while ip <= int(end_ip_suffix):
                ip_address = f'{".".join(start_ip.split(".")[:3])}.{ip}'
                executor.submit(worker, ip_address)
                ip += 1

        # Sort the result list by 'aliveStatus' (True first) and then by 'ip'
        sorted_result = sorted(ip_alive_list, key=lambda x: (not x['aliveStatus'], x['ip']))
        return {'result': sorted_result}

    except Exception as e:
        error = f'Error: {str(e)}'
        return {'error' : error}