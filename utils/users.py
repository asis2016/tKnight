"""
Utility function to retrieve list of users and it's associated terminal.
"""

__author__ = "Ashish S. Maharjan"
__email__ = "hello@amaharjan.de"
__version__ = "1.0"

import psutil


def get_users():
    try:
        users = {}
        for user in psutil.users():
            users['name']= user[0]
            users['terminal']= user[1]
            users['host']= user[2]
            users['started']= user[3]
            users['pid']= user[4]

        return {'result': users}
    
    except Exception as e:
        error = f'Error: {str(e)}'
        return {'error' : error}