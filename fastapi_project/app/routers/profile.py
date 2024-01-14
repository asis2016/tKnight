__author__ = 'amaharjan.de'

from fastapi import APIRouter
import subprocess
from ..logger import log

router = APIRouter()

@router.get('/profile/', tags=['System Info'])
def read_profile():
    '''
    Return "for profile page"
    '''
    log.info('/profile/ requested.')
    #TODO
    

