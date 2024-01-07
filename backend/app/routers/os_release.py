__author__ = 'amaharjan.de'

from fastapi import APIRouter
from utils.os_release import get_os_release
from ..logger import log

router = APIRouter()

@router.get('/os-release/', tags=['System Info'])
def read_os_release():
    '''
    Return OS information from /etc/os-release.
    NOTE: Only tested with Fedora!
    TODO: Test with different distro.
    '''
    log.info('/os-release/ requested.')
    result = get_os_release()
    return result
