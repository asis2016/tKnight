__author__ = 'amaharjan.de'

from fastapi import APIRouter
from utils.sensors import *
from ..logger import log

router = APIRouter()


@router.get('/sensors/temperature/', tags=['Sensors'])
async def read_sensors_temperature():
    '''
    Return hardware temperatures.
    '''
    log.info('/sensors/temperature/ started.')
    result = get_sensors_temperature()
    return result
    

@router.get('/sensors/battery/', tags=['Sensors'])
async def read_sensors_battery():
    '''
    Return battery information.
    '''
    log.info('/sensors/battery/ started.')
    result = get_sensors_battery()
    return result


@router.get('/sensors/fan/', tags=['Sensors'])
async def read_sensors_fan():
    '''
    Return fan information.
    '''
    log.info('/sensors/fan/ started.')
    result = get_sensors_fan()
    return result
