__author__ = 'amaharjan.de'

from fastapi import APIRouter
from utils.traceroute import get_traceroute

router = APIRouter()


@router.post('/traceroute/', tags=['Networking'])
def traceroute(hostname: str):
    '''
    Traceroute endpoint that accepts a POST request with a 'hostname' parameter.
    Returns a JSON response containing traceroute information.
    '''
    result = get_traceroute(hostname)
    return result
    
