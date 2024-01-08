__author__ = 'amaharjan.de'

from fastapi import APIRouter
from utils.lsof import get_lsof
from ..logger import log

router = APIRouter()

@router.get('/lsof/n/i/', tags=['lsof'])
def read_lsof():
    '''
    Return `$ lsof -n -i`
    '''
    log.info('/lsof/n/i/ requested.')
    result = get_lsof()
    return result
