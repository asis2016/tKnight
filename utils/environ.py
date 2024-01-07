"""
Utility function to retrieve env.
Return all environment variables of the OS.
"""

__author__ = "Ashish S. Maharjan"
__email__ = "hello@amaharjan.de"
__version__ = "1.0"

import psutil


def get_environ():
    try:
        env  = psutil.Process().environ()
        return {
            'result': env,
            'total': len(env)
        }
    except Exception as e:
        error = f'Error: {str(e)}'
        return {'error' : error}


