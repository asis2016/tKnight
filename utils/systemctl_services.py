"""
Utility function to retrieve systemctl services.
"""

__author__ = "Ashish S. Maharjan"
__email__ = "hello@amaharjan.de"
__version__ = "1.0"

import subprocess
import re


def get_systemctl_services():
    try:
        systemctl_list = []

        systemctl = subprocess.Popen(['systemctl', 'list-units', '--type=service'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        #decode
        output, _ = systemctl.communicate()
        output_str = output.decode('utf-8')

        # Define a regular expression pattern to match UNIT and DESCRIPTION
        pattern = re.compile(r'^\s*([^ ]+)\s+([^ ]+)\s+([^ ]+)\s+([^ ]+)\s+([^\n]+)', re.MULTILINE)

        # Find all matches in the output, 
        # skipping the first line (headers) and last 5 lines
        matches = pattern.findall(output_str.split('\n', 1)[1].rsplit('\n', 6)[0])

        for unit, load, active, sub, description in matches:
            _sys = {
                'unit': unit,
                'load':load,
                'active': active,
                'sub': sub,
                'description': description
            }
            systemctl_list.append(_sys)

        return {
            'result': systemctl_list,
            'total': str(len(systemctl_list))
        }
    except Exception as e:
        error = f'Error: {str(e)}'
        return {'error' : error}