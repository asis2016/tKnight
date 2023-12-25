__author__ = 'amaharjan.de'

from fastapi import APIRouter
import psutil

router = APIRouter()


@router.get('/environ/', tags=['System Info'])
async def read_environ():
    '''
    Return all environment variables of the OS.
    '''
    env  = psutil.Process().environ()
    return {'result': env}
