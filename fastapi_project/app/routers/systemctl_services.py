__author__ = 'amaharjan.de'

from fastapi import APIRouter
from utils.systemctl_services import get_systemctl_services
from ..logger import log

router = APIRouter()

@router.get('/systemctl/services/', tags=['Systemctl'])
def read_systemctl_services_running():
    '''
    Return `$ systemctl list-units --type=service --state=running`
    '''
    log.info('/systemctl/services/ started.')
    result = get_systemctl_services()
    return result
