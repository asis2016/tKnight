# tKnight
Tux Knight (tKnight) is an Open Source Linux administration monitoring software made in Dango.


## Tech Stack
- Python3 
- Django
- FastAPI
- HTML/CSS
- JavaScript, jQuery
- Shell script
## Setting up tKnight
```bash
$ mkdir tknight
$ cd tknight
$ git clone https://github.com/asis2016/tKnight.git .
```

### 1. Running Django
```bash
$ cd django_project
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip3 install -r requirements.txt

# Now, run the project
(venv) $ python3 manage.py runserver
```

Now, browse http://127.0.0.1:8000/

### 2. Running FastAPI
```bash
$ cd fastapi_project
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip3 install -r requirements.txt

# Now, run the project
(venv) $ uvicorn app.main:app --reload
```

## Contributing
Contributions are always welcome! Please, contact to hello@amaharjan.de

## License
[MIT](./LICENSE)

## References
- [Dark Bootstrap 5 Admin Template](https://github.com/asis2016/bootstrap-5-admin-template)




