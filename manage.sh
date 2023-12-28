#!/bin/bash

# manage.sh run
if [ "$1" = "run" ]; then
    #backend
    gnome-terminal --tab -- bash -c 'cd backend; source venv/bin/activate; uvicorn app.main:app --reload; exec bash'

    #frontend
    gnome-terminal --tab -- bash -c 'cd frontend; source venv/bin/activate; flask run --port 9002 --debug; exec bash'
fi