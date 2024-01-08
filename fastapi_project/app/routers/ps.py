__author__ = 'amaharjan.de'

from fastapi import APIRouter
from utils.ps import get_ps
from ..logger import log

router = APIRouter()


@router.get('/ps/', tags=['System Info'])
def read_ps():
    '''
    Return processes of the OS.
    '''
    log.info('/ps/ requested.')
    result = get_ps()
    return result
    



