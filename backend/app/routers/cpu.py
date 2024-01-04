__author__ = 'amaharjan.de'

from fastapi import APIRouter, WebSocket
import psutil
import time
import asyncio

from ..logger import log

router = APIRouter()


@router.get('/cpu/count/', tags=['CPU'])
async def read_cpu_count():
    '''
    Return CPU count, i.e. core
    '''
    log.info('/cpu/count/ requested.')

    result  = psutil.cpu_count()
    return {'result': result}


async def cpu_data(ws: WebSocket):
    while True:
        cpu_percent_per_core = psutil.cpu_percent(interval=1, percpu=True)
        response_data = {
            f"Core {core + 1}": usage for core, usage in enumerate(cpu_percent_per_core)
        }
        await ws.send_json(response_data)
        await asyncio.sleep(1)

@router.websocket("/cpu/async/")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    await cpu_data(ws)


# @router.get('/cpu/', tags=['CPU'])
# async def read_cpu_percent():
#     '''
#     Return CPU percentage.
#     '''
#     log.info('/cpu/ requested.')

#     result  = psutil.cpu_percent(interval=10, percpu=True)

#     return {
#         'result': result
#     }

