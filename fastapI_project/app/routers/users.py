__author__ = 'amaharjan.de'

from fastapi import APIRouter
from utils.users import get_users

router = APIRouter()


@router.get('/users/', tags=['System Info'])
def read_users():
    '''
    Return list of users and it's associated terminal.
    '''
    result = get_users()
    return result


