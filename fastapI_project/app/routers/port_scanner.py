__author__ = 'amaharjan.de'

from fastapi import APIRouter
import socket
import threading

router = APIRouter()


@router.post('/scan-port/', tags=['Networking'])
async def port_scanner(hostname: str):
    '''
    Return a list of open ports of an IP address.

    Important:  
    Unauthorized port scanning can be detected and may lead to serious consequences.
    Only scan ports that you are allowed to!
    '''
    START_PORT = 1
    END_PORT = 65535
    
    open_ports = []
    threads = []

    def scan_port(port):
        print(f'Scanning port: {port}')
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((hostname, port))

        if result == 0:
            open_ports.append(port)

        sock.close()

    def worker(port):
        scan_port(port)

    for port in range(START_PORT, END_PORT + 1):
        thread = threading.Thread(target=worker, args=(port,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return {
        'result': open_ports,
        'totalOpenPorts': len(open_ports)
    }
