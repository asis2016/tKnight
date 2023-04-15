#!/bin/bash
#
# Author: Lion
# Script name: start.sh
# Usage: ./start.sh
# Date: 15.04.2023
# Description: This script will start `uknight`.
# URL: https://github.com/asis2016/u_knight 

# Rename .env.bak to .env
mv ./.env.bak  ./.env

#Read .env
source ./.env

#Start the project
python3 uknight/manage.py runserver