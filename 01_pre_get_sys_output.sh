#!/bin/bash

# out dir
out_dir="./uknight/out"

#
#
# Run essential `.out`files

# crontab
crontab -l > "$out_dir/crontab.out"

# df
df / -h > "$out_dir/df.out"

# dpkg
dpkg --list | tail -n +4 > "$out_dir/dpkg.out"

# du
sudo du  / -h -d 1 --total > "$out_dir/du.out"

# free
free -ht > "$out_dir/free.out"

# hostnamectl
hostnamectl > "$out_dir/hostnamectl.out"

# last
last -n 5 --dns > "$out_dir/last.out"

# ps
ps > "$out_dir/ps.out"

# route
route > "$out_dir/route.out"

# ss
ss -ntl > "$out_dir/ss.out"

# ssh
ssh -V > "$out_dir/ssh.out"

# ip
ip -s -h a > "$out_dir/ip.out"

# iwconfig
iwconfig > "$out_dir/iwconfig.out"

#whoami
whoami > "$out_dir/whoami.out"

#
#
# systemctl
systemctl list-units > "$out_dir/systemctl.out"

#Retrieve top services status
function get_top_services_status(){
    local services=(
        apache2
        mysql
        docker
        slapd
    )
    local output=()
    
    for service in "${services[@]}"
    do
    status=$(systemctl is-active $service)
    output+=("{\"service\": \"$service\", \"status\": \"$status\"}")
    done

    printf '%s\n' "${output[@]}" | jq -s .
}

echo -e "\n[info] Getting top services status."
get_top_services_status > "$out_dir/top_services.json"



