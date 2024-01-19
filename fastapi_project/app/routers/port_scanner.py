__author__ = 'amaharjan.de'

from fastapi import APIRouter


router = APIRouter()


@router.post('/scan-port/', tags=['Networking'])
async def port_scanner(hostname: str):
    '''
    Return a list of open ports of an IP address.

    Important:  
    Unauthorized port scanning can be detected and may lead to serious consequences.
    Only scan ports that you are allowed to!
    '''
    #todo
