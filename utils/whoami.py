"""
Utility function to retrieve the current username using the 'whoami' command.
"""

__author__ = "Ashish S. Maharjan"
__email__ = "hello@amaharjan.de"
__version__ = "1.0"

import subprocess

def get_whoami():
    try:
        result = subprocess.check_output(['whoami'], text=True).strip()
        return {'result' : result}
    except Exception as e:
        error = f'Error: {str(e)}'
        return {'error' : error}