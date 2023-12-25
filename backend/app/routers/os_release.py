__author__ = 'amaharjan.de'

from fastapi import APIRouter
import subprocess

router = APIRouter()

@router.get('/os-release/', tags=['System Info'])
def read_os_release():
    '''
    Return OS information from /etc/os-release.
    NOTE: Only tested with Fedora!
    TODO: Test with different distro.
    '''
    output = subprocess.check_output(['cat', '/etc/os-release'], universal_newlines=True) #universal_newlines for normalizing \n, etc.
    
    os_release_dict = {}

    for line in output.splitlines():
            key, value = line.split('=', 1)
            os_release_dict[key.strip()] = value.strip().strip('"')
    
    return {'result': os_release_dict}
