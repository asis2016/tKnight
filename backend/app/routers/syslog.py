__author__ = 'amaharjan.de'

from fastapi import APIRouter
import subprocess
import re

router = APIRouter()

@router.get('/syslog/', tags=['System Info'])
def read_syslog():
    '''
    Return syslog from logs/app.log
    '''
    try:
        log_file_path = './logs/app.log'
        log_entries = []

        with open(log_file_path, 'r') as log_file:
            for line in log_file:
                pattern = r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] \[(\w+)\] \[(.*?)\]'
                match = re.match(pattern, line)

                if match:
                    datestamp, level, message = match.groups()
                    log_entry = {
                        'datestamp': datestamp,
                        'level': level,
                        'message': message
                    }
                    log_entries.append(log_entry)

        return {'result': log_entries}
    
    except subprocess.CalledProcessError as e:
        return {'error': 'Failed to run whoami.'}
