"""
Utility function to retrieve bootime.
"""

__author__ = "Ashish S. Maharjan"
__email__ = "hello@amaharjan.de"
__version__ = "1.0"

import datetime
import psutil


def get_bootime():
    try:
        bootime = psutil.boot_time()
        result = datetime.datetime.fromtimestamp(bootime).strftime('%Y-%m-%d %H:%M:%S')
        return {'result':result}
    except Exception as e:
        error = f'Error: {str(e)}'
        return {'error' : error}