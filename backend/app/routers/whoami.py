__author__ = 'amaharjan.de'

from fastapi import APIRouter
import subprocess
from ..logger import log

router = APIRouter()

@router.get('/whoami/', tags=['System Info'])
def read_whoami():
    '''
    Return `whoami` from the OS.
    '''
    log.info('read_whoami started.')
    try:
        result = subprocess.check_output(['whoami'], text=True).strip()
        return {'result': result}
    except subprocess.CalledProcessError as e:
        log.error(f'Error running whoami: {e}')
        return {'error': 'Failed to run whoami.'}
