#!/bin/bash

# out dir
output_dir="./uknight/out"

#
#
# Run essential `.out`files

# crontab
crontab -l > "$output_dir/crontab.out"

# df
df / -h > "$output_dir/df.out"

# dpkg
dpkg --list | tail -n +4 > "$output_dir/dpkg.out"

# du
sudo du / -h -d 1 > "$output_dir/du.out"

# free
free -ht > "$output_dir/free.out"

# hostnamectl
hostnamectl > "$output_dir/hostnamectl.out"

# last
last -n 5 --dns > "$output_dir/last.out"

# ps
ps > "$output_dir/ps.out"

# route
route > "$output_dir/route.out"

# ss
ss -ntl > "$output_dir/ss.out"

# ssh
ssh -V > "$output_dir/ssh.out"

# ip
ip -s -h a > "$output_dir/ip.out"

# iwconfig
iwconfig > "$output_dir/iwconfig.out"



