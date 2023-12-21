from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import boottime, disk, environ, ifconfig, ip_scanner, ps, sensors, speed_test_cli, traceroute, users, whoami

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

app.include_router(boottime.router)
app.include_router(disk.router)
app.include_router(environ.router)
app.include_router(ifconfig.router)
app.include_router(ip_scanner.router)
app.include_router(ps.router)
app.include_router(sensors.router)
app.include_router(speed_test_cli.router)
app.include_router(traceroute.router)
app.include_router(users.router)
app.include_router(whoami.router)


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}