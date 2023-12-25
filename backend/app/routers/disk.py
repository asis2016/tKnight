__author__ = 'amaharjan.de'

from fastapi import APIRouter
import psutil
import subprocess
import re

router = APIRouter()


@router.get('/disk/usage/', tags=['Disk'])
async def read_disk_usage():
    '''
    Return disk usage statistics.
    '''
    du = psutil.disk_usage('/')
    result = dict(du._asdict())

    return {'result': result}


@router.get('/disk/partition/', tags=['Disk'])
async def read_disk_partition():
    '''
    Return disk partition statistics.
    '''
    result = []
    data = subprocess.check_output(['df', '-h']).decode('utf-8')

    # Skip the header line
    lines = data.split('\n')[1:]

    for line in lines:
        if line.strip() == '':
            continue
        columns = re.split(r'\s+', line)
        filesystem, size, used, avail, use_percent, mounted_on = columns
        
        entry = {
            'Filesystem': filesystem,
            'Size': size,
            'Used': used,
            'Avail': avail,
            'Use%': use_percent,
            'Mounted on': mounted_on
        }

        result.append(entry)
    
    return {'result': result}
