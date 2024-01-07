"""
Utility function to retrieve ifconfig information.
Return just the default interface device dictionary.
"""

__author__ = "Ashish S. Maharjan"
__email__ = "hello@amaharjan.de"
__version__ = "1.0"

import ifcfg

def get_ifconfig():
    try:
        result = ifcfg.default_interface()
        return {'result' : result}
    except Exception as e:
        error = f'Error: {str(e)}'
        return {'error' : error}