from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import (
    boottime, 
    disk, 
    environ, 
    ifconfig, 
    ip_scanner,
    lsof,
    os_release, 
    port_scanner,
    ps, 
    sensors, 
    speed_test_cli, 
    systemctl_services,
    traceroute, 
    users, 
    whoami
)

app = FastAPI()

origins = [
    "http://localhost:9002",
    "http://localhost:8000",
    "http://127.0.0.1:9002",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

routers = [
    boottime.router,
    disk.router,
    environ.router,
    ifconfig.router,
    ip_scanner.router,
    lsof.router,
    os_release.router,
    port_scanner.router,
    ps.router,
    sensors.router,
    speed_test_cli.router,
    systemctl_services.router,
    traceroute.router,
    users.router,
    whoami.router
]

for router in routers:
    app.include_router(router)
