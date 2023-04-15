#!/bin/bash
#
# Author: Lion
# Script name: 00_pre_install_linux_packages.sh
# Usage: ./00_pre_install_linux_packages.sh
# Date: 15.04.2023
# Description: This script is a pre-requisite for `uknight`.
# URL: https://github.com/asis2016/u_knight 


sudo apt -y update

packages=(
    apache2
    cron
    elinks
    iputils-ping
    jq
    ldap-utils
    lsof
    man
    mysql-server
    net-tools
    nmap
    python3-pytest
    slapd
    tmux
    tree
    vi
    wget
    wireless-tools
)

for package in "${packages[@]}"
do
    if ! dpkg -s "$package" > /dev/null 2>&1; then
        echo "[info] Installing $package"
        sudo apt-get -y install "$package"
    else
        echo "[info] $package is already installed, skipping"
    fi
done






 
