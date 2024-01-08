__author__ = 'amaharjan.de'

from fastapi import APIRouter
from utils.boottime import get_bootime
from ..logger import log

router = APIRouter()

@router.get('/boottime/', tags=['System Info'])
def read_boottime():
    '''
    Return boot time info from the OS.
    '''
    log.info('/bootime/ requested.')
    result = get_bootime()
    return result
