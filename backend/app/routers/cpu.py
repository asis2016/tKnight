__author__ = 'amaharjan.de'

from fastapi import APIRouter, WebSocket
from utils.cpu import get_cpu_count
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
    result  = get_cpu_count()
    return result


# ws
async def cpu_data(ws: WebSocket):
    while True:
        cpu_percent_per_core = psutil.cpu_percent(interval=1, percpu=True)
        response_data = {
            f"Core {core + 1}": usage for core, usage in enumerate(cpu_percent_per_core)
        }
        await ws.send_json(response_data)
        await asyncio.sleep(2)

@router.websocket("/cpu/async/")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    await cpu_data(ws)
