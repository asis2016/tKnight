__author__ = 'amaharjan.de'

from fastapi import APIRouter
import psutil

router = APIRouter()


@router.get('/users/', tags=['System Info'])
def read_users():
    '''
    Return list of users and it's associated terminal.
    '''
    users = {}

    for user in psutil.users():
        users['name']= user[0]
        users['terminal']= user[1]
        users['host']= user[2]
        users['started']= user[3]
        users['pid']= user[4]

    return {'result': users}
