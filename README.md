# Introduction
Tux Knight (tKnight) is a Linux administration monitoring software made in FastAPI and Flask.

## Tech Stack
- Python, FastAPI, HTML/CSS, JavaScript, jQuery, Shell script


## TOC
[I. Tech Stack](#tech-stack)<br>
[II. Setting up tKnight](#setting-up-tknight)<br>
[III. Running tKnight](#running-tknight)<br>
[IV. API Reference](#api-reference)<br>
[V. Demo](#demo)<br>
[VI. Contributing](#contributing)<br>
[VII. License](#license)<br>
[VIII. References](#references)<br>
## Setting up tKnight
```
$ mkdir tknight
$ cd tknight
$ git clone https://github.com/asis2016/tKnight.git .
```

1. Backend
```
$ cd backend
$ python3 -m venv venv
$ pip install -r requirements.txt
```

2. Frontend
```
$ cd frontend
$ python3 -m venv venv
$ pip install -r requirements.txt
```

## Running tKnight
1. Backend
```bash
$ cd backend
$ source venv/bin/activate
(venv) $ uvicorn app.main:app --reload
```

2. Frontend
```bash
$ cd frontend
$ source venv/bin/activate
(venv) $ flask run --port 9002 --debugger
```

Or, simply run `./manage.sh run`
```
$ ./manage.sh run
```

Now, browse http://127.0.0.1:9002/
## API Reference
#### Get Boottime
```http
  GET /boottime/
```

#### Get Disk partition info
```http
  GET /disks/partition
```

#### Get Disk usage info
```http
  GET /disks/usage
```

#### Get Environment variables
```http
  GET /environ/
```

#### Get ifconfig
```http
  GET /ifconfig/
```

#### Get OS information
```http
  GET /os-release/
```

#### Get all running Processes
```http
  GET /ps/
```

#### Get Battery sensors  
```http
  GET /sensors/battery/
```

#### Get Fan sensors  
```http
  GET /sensors/fan/
```

#### Get Temperature sensors  
```http
  GET /sensors/temperature/
```

#### Post Scan IP
```http
  POST /scan-ip/?start_ip=192.168.0.1&end_ip=192.168.0.254
```
| Key | Value     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `start_ip`  | `string` | start_ip is required. |
| `end_ip`  | `string` | end_ip is required. |

#### Post Scan port
```http
  POST /scan-port/?hostname=example.com
```
| Key | Value     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `hostname`  | `string` | Hostname is required. |

#### Get Speedtest
```http
  GET /speed-test/
```

#### Post Traceroute
```http
  POST /traceroute/?hostname=example.com
```
| Key | Value     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `hostname`  | `string` | Hostname is required. |

#### Get users
```http
  GET /users/
```

#### Get whoami
```http
  GET /whoami/
```

## Features
WIP

## Demo
WIP

## logs

To view the logs for backend
```
$ tail -f backend/logs/app.log
```
## Contributing
Contributions are always welcome! Please, contact to hello@amaharjan.de

## License
[MIT](./LICENSE)

## References
- [Corona Admin template](https://www.bootstrapdash.com/product/corona-admin-template)




