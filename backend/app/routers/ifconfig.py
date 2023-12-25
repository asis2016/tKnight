__author__ = 'amaharjan.de'

from fastapi import APIRouter
import ifcfg

router = APIRouter()


@router.get('/ifconfig/', tags=['Networking'])
def read_ifconfig():
    '''
    Return just the default interface device dictionary.
    '''
    result = ifcfg.default_interface()
    return {'result': result}
