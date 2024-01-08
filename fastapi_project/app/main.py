from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Get the current working directory
import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))

print(current_dir)

# Append the project path to sys.path
project_path = os.path.join(current_dir, "../..")  # Assuming your project is one level above the main script
sys.path.append(project_path)


from app.routers import (
    boottime,
    cpu,
    disk,
    environ,
    ifconfig,
    ip_scanner,
    lsof,
    os_release, 
    port_scanner,
    ps,
    profile,
    sensors, 
    speed_test_cli, 
    systemctl_services,
    syslog,
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
    cpu.router,
    disk.router,
    environ.router,
    ifconfig.router,
    ip_scanner.router,
    lsof.router,
    os_release.router,
    port_scanner.router,
    ps.router,
    profile.router,
    sensors.router,
    speed_test_cli.router,
    systemctl_services.router,
    syslog.router,
    traceroute.router,
    users.router,
    whoami.router
]

for router in routers:
    app.include_router(router)
