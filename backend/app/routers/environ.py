__author__ = 'amaharjan.de'

from fastapi import APIRouter
from ..logger import log
from utils.environ import get_environ

router = APIRouter()

@router.get('/environ/', tags=['System Info'])
async def read_environ():
    '''
    Return all environment variables of the OS.
    '''
    log.info('/environ/ requested.')
    result = get_environ()
    return result
    
    
