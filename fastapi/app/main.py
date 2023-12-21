from fastapi import FastAPI
from app.routers import environ, ip_scanner, ps, sensors 

app = FastAPI()

origins = [
    "http://localhost:9002",
    "http://localhost:8000",
    "http://127.0.0.1:9002",
    "http://127.0.0.1:8000",
]

app.include_router(environ.router)
app.include_router(ip_scanner.router)
app.include_router(ps.router)
app.include_router(sensors.router)


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}