__author__ = 'amaharjan.de'

from fastapi import APIRouter
from utils.whoami import get_whoami
from ..logger import log

router = APIRouter()

@router.get('/whoami/', tags=['System Info'])
def read_whoami():
    '''
    Return `whoami` from the OS.
    '''
    log.info('read_whoami started.')
    result = get_whoami()
    return {'result': result}
