__author__ = 'amaharjan.de'

from fastapi import APIRouter
import subprocess
import re
from ..logger import log

router = APIRouter()

@router.get('/systemctl/services/', tags=['Systemctl'])
def read_systemctl_services_running():
    '''
    Return `$ systemctl list-units --type=service --state=running`
    '''
    log.info('read_systemctl_services_running started.')

    systemctl = subprocess.Popen(['systemctl', 'list-units', '--type=service'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    #decode
    output, _ = systemctl.communicate()
    output_str = output.decode('utf-8')

    # Define a regular expression pattern to match UNIT and DESCRIPTION
    pattern = re.compile(r'^\s*([^ ]+)\s+([^ ]+)\s+([^ ]+)\s+([^ ]+)\s+([^\n]+)', re.MULTILINE)

    # Find all matches in the output, 
    # skipping the first line (headers) and last 5 lines
    matches = pattern.findall(output_str.split('\n', 1)[1].rsplit('\n', 6)[0])

    systemctl_list = []

    for unit, load, active, sub, description in matches:
        _sys = {
            'unit': unit,
            'load':load,
            'active': active,
            'sub': sub,
            'description': description
        }
        systemctl_list.append(_sys)

    return {'result': systemctl_list}
