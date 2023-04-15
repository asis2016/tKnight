# u_knight
`u_knight` is the Ubuntu OS administration monitoring software made in Django. The web application provides web interface to manage and monitor Ubuntu system.

Project status: WIP

## Installation

```bash
$ mkdir u_knight ; cd u_knight ; git clone https://github.com/asis2016/u_knight.git .
```

```bash
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
```

## Start the project

`.env.bak` is important before you start the project. Hence, fill out .env with relevant information.

Note: `.env.bak` will be converted to `.env`

Now, start the project:
```bash
(venv) $ ./start.sh
```

## .gitignore

```
.gitignore
venv
```




