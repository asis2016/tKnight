__author__ = 'amaharjan.de'

from fastapi import APIRouter
import subprocess

router = APIRouter()


@router.get('/whoami/', tags=['System Info'])
def read_whoami():
    '''
    Return `whoami` from the OS.
    '''
    result = subprocess.check_output(['whoami'], text=True).strip()
    return {'result': result}
