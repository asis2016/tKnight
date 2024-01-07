__author__ = 'amaharjan.de'

from fastapi import APIRouter
from utils.disk_usage import get_disk_usage
from utils.disk_partition import get_disk_partition
from ..logger import log

router = APIRouter()

@router.get('/disk/usage/', tags=['Disk'])
async def read_disk_usage():
    '''
    Return disk usage statistics.
    '''
    log.info('/disk/usage/ requested.')
    result = get_disk_usage()
    return result


@router.get('/disk/partition/', tags=['Disk'])
async def read_disk_partition():
    '''
    Return disk partition statistics.
    '''
    log.info('/disk/partition/ requested.')
    result = get_disk_partition()
    return result
