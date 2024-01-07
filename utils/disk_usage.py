"""
Utility function to retrieve disk usage statistics.
"""

__author__ = "Ashish S. Maharjan"
__email__ = "hello@amaharjan.de"
__version__ = "1.0"

import psutil


def get_disk_usage():
    try:
        du = psutil.disk_usage('/')
        result = dict(du._asdict())
        return {'result' : result}
    except Exception as e:
        error = f'Error: {str(e)}'
        return {'error' : error}