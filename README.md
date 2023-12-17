# Introduction

Tux Knight (tKnight) is a Linux administration monitoring software made in Django and Flask.

## Setting up tKnight

### Setting up backend
```bash
$ cd backend
$ python -m venv venv
$ pip install -r requirements.txt
```

### Setting up backend
```bash
$ cd backend
$ python -m venv venv
$ pip install -r requirements.txt
```

## Running tKnight

### Running the backend
```bash
$ cd backend
$ source venv/bin/activate
$ cd tux
$ python manage.py runserver
```


### Running the frontend
```bash
$ cd frontend
$ source venv/bin/activate
$ flask run --port 9002
```


## REST APIs

### Disk
- GET [/api/v1/disks/usage](http://127.0.0.1:8000/api/v1/disks/usage)
- GET [/api/v1/disks/partition](http://127.0.0.1:8000/api/v1/disks/partition)

### Process
- GET [/api/v1/processes/](http://127.0.0.1:8000/api/v1/processes/)
- GET [/api/v1/processes/environ](http://127.0.0.1:8000/api/v1/processes/environ)

### Sensors
- GET [/api/v1/sensors/temperature](http://127.0.0.1:8000/api/v1/sensors/temperature)
- GET [/api/v1/sensors/battery](http://127.0.0.1:8000/api/v1/sensors/battery)
- GET [/api/v1/sensors/fans](http://127.0.0.1:8000/api/v1/sensors/fans)

### Systeminfo
- GET [/api/v1/sysinfo/boottime](http://127.0.0.1:8000/api/v1/sysinfo/boottime)
- GET [/api/v1/sysinfo/users](http://127.0.0.1:8000/api/v1/sysinfo/users)
