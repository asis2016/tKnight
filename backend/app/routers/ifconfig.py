__author__ = 'amaharjan.de'

from fastapi import APIRouter
from utils.ifconfig import get_ifconfig
from ..logger import log

router = APIRouter()

@router.get('/ifconfig/', tags=['Networking'])
def read_ifconfig():
    '''
    Return just the default interface device dictionary.
    '''
    log.info('/ifconfig/ requested.')
    result = get_ifconfig()
    return result
