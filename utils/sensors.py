"""
Utility function to retrieve various sensors.
"""

__author__ = "Ashish S. Maharjan"
__email__ = "hello@amaharjan.de"
__version__ = "1.0"

import psutil


def get_sensors_temperature():
    try:
        temperature = psutil.sensors_temperatures()
        return {
            'result' : temperature,
            'total': len(temperature)
        }
    except Exception as e:
        error = f'Error: {str(e)}'
        return {'error' : error}


def get_sensors_battery():
    try:
        battery = psutil.sensors_battery()
        battery_dict = dict(battery._asdict())
        return {'result': battery_dict}
    except Exception as e:
        error = f'Error: {str(e)}'
        return {'error' : error}


def get_sensors_fan():
    try:
        fan = psutil.sensors_fans()
        return {'result': fan}
    except Exception as e:
        error = f'Error: {str(e)}'
        return {'error' : error}