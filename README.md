# Introduction
Tux Knight (tKnight) is a Linux administration monitoring software made in FastAPI and Flask.

## TOC
[I. Tech Stack](#tech-stack)<br>
[II. Setting up tKnight](#setting-up-tknight)<br>
[III. Running tKnight](#running-tknight)<br>
[IV. API Reference](#api-reference)<br>
[V. Demo](#demo)<br>
[VI. Contributing](#contributing)<br>
[VII. License](#license)<br>
[VIII. References](#references)<br>

## Tech Stack
- Python, FastAPI, HTML/CSS, JavaScript, jQuery, Shell script

## Setting up tKnight
### 1. Setting up backend
```bash
$ cd backend
$ python -m venv venv
$ pip install -r requirements.txt
```

### 2. Setting up backend
```bash
$ cd backend
$ python -m venv venv
$ pip install -r requirements.txt
```

## Running tKnight
### 1. Running the backend
```bash
$ cd backend
$ source venv/bin/activate
(venv) backend$ ./start.sh
```

### 2. Running the frontend
```bash
$ cd frontend
$ source venv/bin/activate
(venv) frontend$ ./start.sh
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


## Demo
WIP

## Contributing
Contributions are always welcome! Please, contact to hello@amaharjan.de

## License
[MIT](./LICENSE)

## References
- [Corona Admin template](https://www.bootstrapdash.com/product/corona-admin-template)



