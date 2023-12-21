from fastapi import FastAPI
from app.routers import boottime, disk, environ, ifconfig, ip_scanner, ps, sensors, users, whoami

app = FastAPI()

origins = [
    "http://localhost:9002",
    "http://localhost:8000",
    "http://127.0.0.1:9002",
    "http://127.0.0.1:8000",
]

app.include_router(boottime.router)
app.include_router(disk.router)
app.include_router(environ.router)
app.include_router(ifconfig.router)
app.include_router(ip_scanner.router)
app.include_router(ps.router)
app.include_router(sensors.router)
app.include_router(users.router)
app.include_router(whoami.router)


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}