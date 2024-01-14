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

## logs

To view the logs for backend
```
$ tail -f backend/logs/app.log
```