#!/bin/bash

# Run essential `.out`files

# hostnamectl
hostnamectl > ./uknight/static/out/hostnamectl.out

# Start the project
python3 uknight/manage.py runserver