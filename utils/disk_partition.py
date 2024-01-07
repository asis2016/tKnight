"""
Utility function to retrieve disk partition statistics.
"""

__author__ = "Ashish S. Maharjan"
__email__ = "hello@amaharjan.de"
__version__ = "1.0"

import subprocess
import re


def get_disk_partition():
    result = []
    try:
        data = subprocess.check_output(['df', '-h']).decode('utf-8')

        # Skip the header line
        lines = data.split('\n')[1:]

        for line in lines:
            if line.strip() == '':
                continue
            columns = re.split(r'\s+', line)
            filesystem, size, used, avail, use_percent, mounted_on = columns
            
            entry = {
                'Filesystem': filesystem,
                'Size': size,
                'Used': used,
                'Avail': avail,
                'Use%': use_percent,
                'Mounted on': mounted_on
            }
            result.append(entry)
        return {
            'result': result,
            'total': len(result)
        }
    
    except Exception as e:
        error = f'Error: {str(e)}'
        return {'error' : error}