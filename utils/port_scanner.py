"""
Utility function to scan ports.
"""

__author__ = "Ashish S. Maharjan"
__email__ = "hello@amaharjan.de"
__version__ = "1.0"

import socket
import threading


def get_port_scanner(hostname: str):
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
