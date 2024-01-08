__author__ = 'amaharjan.de'

from fastapi import APIRouter
import subprocess

router = APIRouter()


@router.get('/speed-test/', tags=['Networking'])
def read_speed_test_cli():
    '''
    Return internet speed test, i.e., upload, download and ping time taken.
    '''
    bytes_data = subprocess.check_output(['speedtest-cli', '--simple'])
    string_data = bytes_data.decode('utf-8')
    lines = string_data.split('\n')

    result = {}

    for line in lines:
        if line.strip():  # Ignore empty lines
            key, value = line.split(': ')
            result[key.lower()] = value

    return {'result': result}
