__author__ = 'amaharjan.de'

from fastapi import APIRouter
import subprocess
import re
from ..logger import log

router = APIRouter()

@router.get('/lsof/n/i/', tags=['lsof'])
def read_lsof():
    '''
    Return `$ lsof -n -i`
    '''
    log.info('read_lsof started.')

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
