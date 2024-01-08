__author__ = 'amaharjan.de'

from fastapi import APIRouter
from utils.ip_scanner import get_ips
from ..logger import log

router = APIRouter()

@router.post('/scan-ip/', tags=['Networking'])
async def ip_scanner(start_ip: str, end_ip: str):
    '''
    Return a list of 'alive' IP addresses.

    :param start_ip:    The starting IP address.
    :param end_ip:      The end IP address.
    '''
    log.info('/scan-ip/ requested.')
    result = get_ips(start_ip, end_ip)
    return result

