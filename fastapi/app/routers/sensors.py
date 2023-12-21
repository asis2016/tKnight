__author__ = 'amaharjan.de'

from fastapi import APIRouter
import psutil

router = APIRouter()


@router.get('/sensors/temperature/', tags=['Sensors'])
async def sensors_temperature():
    '''
    Return hardware temperatures.
    '''
    temperature = psutil.sensors_temperatures()
    return {'result' : temperature}


@router.get('/sensors/battery/', tags=['Sensors'])
async def sensors_battey():
    '''
    Return battery information.
    '''
    battery = psutil.sensors_battery()
    battery_dict = dict(battery._asdict())
    
    return {'result': battery_dict}


@router.get('/sensors/fan/', tags=['Sensors'])
async def sensors_fan():
    '''
    Return fan information.
    '''
    fan = psutil.sensors_fans()
    return {'result': fan}