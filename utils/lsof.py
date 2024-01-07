"""
Utility function to `lsof -n -i`.
"""

__author__ = "Ashish S. Maharjan"
__email__ = "hello@amaharjan.de"
__version__ = "1.0"

import subprocess


def get_lsof():
    try:
        def parse_lsof_output(output):
                lines = output.strip().split('\n')
                headers = lines[0].split()
                data = []

                for line in lines[1:]:
                    values = line.split()
                    data.append({headers[i]: values[i] for i in range(len(headers))})
                return data

        systemctl = subprocess.Popen(['lsof', '-n', '-i'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output, _ = systemctl.communicate()
        output_str = output.decode('utf-8')
        parsed_data = parse_lsof_output(output_str)
        
        return {
            'result': parsed_data,
            'total': len(parsed_data)
        }
    except Exception as e:
        error = f'Error: {str(e)}'
        return {'error' : error}