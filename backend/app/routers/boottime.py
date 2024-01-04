__author__ = 'amaharjan.de'

from fastapi import APIRouter
import psutil
import datetime
from ..logger import log

router = APIRouter()

@router.get('/boottime/', tags=['System Info'])
def read_boottime():
    '''
    Return boot time info from the OS.
    '''
    log.info('/bootime/ requested.')

    bootime = psutil.boot_time()
    result = datetime.datetime.fromtimestamp(bootime).strftime('%Y-%m-%d %H:%M:%S')
    return {'result': result}
