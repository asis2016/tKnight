"""
Utility function to os related info.
NOTE: Only tested with Fedora!
    TODO: Test with different distro.
"""

__author__ = "Ashish S. Maharjan"
__email__ = "hello@amaharjan.de"
__version__ = "1.0"

import subprocess


def get_os_release():
    try:
        output = subprocess.check_output(['cat', '/etc/os-release'], universal_newlines=True) #universal_newlines for normalizing \n, etc.
        os_release_dict = {}
        for line in output.splitlines():
                key, value = line.split('=', 1)
                os_release_dict[key.strip()] = value.strip().strip('"')
        result = os_release_dict
        return {
            "result": result
        }
    except Exception as e:
        error = f'Error: {str(e)}'
        return {'error' : error}
