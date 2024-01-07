"""
Utility function to retrieve CPU information.
"""

__author__ = "Ashish S. Maharjan"
__email__ = "hello@amaharjan.de"
__version__ = "1.0"

import psutil


def get_cpu_count():
    try:
        result = psutil.cpu_count()
        return {'result': result}
    except Exception as e:
        error = f'Error: {str(e)}'
        return {'error' : error}