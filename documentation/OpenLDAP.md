# OpenLDAP

This documentations shows you how to install and use OpenLDAP client/server on Raspberry PI.

## Installation on RaspberryPI
First `192.168.1.2` (your Raspberry IP address) to the hosts file.
```
$ echo "192.168.1.2  uknightldapserver.example.com  uknightldapserver" | sudo tee -a /etc/host
```

Install `ldap-utils` and `slapd`
```
$ sudo apt install -y ldap-utils slapd

Administrator password: password123456
```

Investigate sockets, check if there is 389 port running
```
$ ss -ntl
```

Configure `slapd`
```
$ sudo dpkg-reconfigure slapd

Omit OpenLDAP server configuration?  No
DNS domain name:  example.com
Organization name:  example.com
Administrator password:  password123456
Do you want the database to be removed when slapd is purged?  No
Move old database?  Yes
```

Add "upper level" structure:
```
$ ldapadd -x -W -D cn=admin,dc=example,dc=com  -f ./structure.ldif
```

```
-x  simple authentication
-W  prompt for bind password
-D  bind DN
-f  file (read operation)
```
