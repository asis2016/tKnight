"""
Utility function to retrieve ps.
"""

__author__ = "Ashish S. Maharjan"
__email__ = "hello@amaharjan.de"
__version__ = "1.0"

import psutil
import datetime

   
def get_ps():
    '''
    Return processes of the OS.
    '''
    try:
        processes_list = []
        status_count = {}

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

                # Count status
                status = proc.status()
                status_count[status] = status_count.get(status, 0) + 1

        return {
            'result': processes_list,
            'page_title': 'Processes',
            'status_count': status_count,
            'total': len(processes_list)
        }
    except Exception as e:
        error = f'Error: {str(e)}'
        return {'error' : error}