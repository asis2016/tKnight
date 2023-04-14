import os
from django.views.generic import TemplateView
from django.conf import settings
import subprocess

def ip_address():
    """ $ ip -s -h a > Linux IPv4 protocol implementation."""
    with open(os.path.join(settings.SHELL_SCRIPT_DIRS, "ip.out")) as data:
        ip_address = data.read()
    return ip_address


def iw_config():
    """ $ iwconfig > configure a wireless network interface."""
    with open(os.path.join(settings.SHELL_SCRIPT_DIRS, "iwconfig.out")) as data:
        iw_config = data.read()
    return iw_config


def disk_free():
    """$ df / -h > Displays file system disk space usage. """
    with open(os.path.join(settings.SHELL_SCRIPT_DIRS, "df.out")) as data:
        df = data.read()
    return df


def disk_usage():
    """$ du / -h -d 1 > estimate file space usage (-d: directory level 1)"""
    with open(os.path.join(settings.SHELL_SCRIPT_DIRS, "du.out"), "r") as data:
        disk_usage_data = data.read()
    return disk_usage_data


def free_memory():
    """$ free -ht > Display amount of free and used memory in the system."""
    with open(os.path.join(settings.SHELL_SCRIPT_DIRS, "free.out"), "r") as data:
        free_memory_data = data.read()
    return free_memory_data


def hostnamectl():
    """
    "Query and change the system hostname and related settings."
    """
    with open(os.path.join(settings.SHELL_SCRIPT_DIRS, "hostnamectl.out"), "r") as data:
        hostnamectl = data.read()
    return hostnamectl


def ps():
    """
    """
    ps_file = os.path.join(settings.SHELL_SCRIPT_DIRS, "ps.out")
    with open(ps_file) as file:
        ps = file.read()
    return ps


def routing_table():
    """ $ route > show the IP routing table. """
    route_r_file = os.path.join(settings.SHELL_SCRIPT_DIRS, "route.out")

    with open(route_r_file) as routes:
        route_table = routes.read()
    return route_table

def ss():
    """
    """
    ss_file = os.path.join(settings.SHELL_SCRIPT_DIRS, "ss.out")
    with open(ss_file) as file:
        ss = file.read()
    return ss

# todo
def systemctl_is_active():
    """
    """
    services = ["docker", "apache2"]
    for service in services:
        x = subprocess.check_output(["systemctl", "is-active", service]).decode("utf-8")
        print(x)


class DashboardView(TemplateView):
    template_name = "home.html"

    print(settings.SHELL_SCRIPT_DIRS)

    def get_context_data(self, *args, **kwargs):
        context = super(DashboardView, self).get_context_data(*args, **kwargs)
        context["whoami"] = subprocess.check_output(["whoami"]).decode("utf-8")
        context["curl_ifconfig_dot_me"] = subprocess.check_output(["curl", "ifconfig.me"]).decode("utf-8")

        context["apache_is_active"] = subprocess.check_output(
            ["systemctl", "is-active", "--quiet", "apache2", "&&", "echo", "active"]).decode("utf-8")

        context["system_info"] = {"kernel": subprocess.check_output(["uname", "-r"]).decode("utf-8"),
                                  "uptime": subprocess.check_output(["uptime", "-p"]).decode("utf-8")}

        context["disk_usage"] = disk_usage()
        context["disk_free"] = disk_free()
        context["free_memory_data"] = free_memory()
        context["hostnamectl"] = hostnamectl()
        context["ip_address"] = ip_address()
        context["iw_config"] = iw_config()
        context["ps"] = ps()
        context["routing_table"] = routing_table()
        context["ss"] = ss()
        context["uptime"] = subprocess.check_output(["uptime"]).decode("utf-8")

        # systemctl
        #systemctl_is_active()


        # shows a listing (5) of last logged in users
        with open(os.path.join(settings.SHELL_SCRIPT_DIRS, "last.out"), "r") as f:
            context["last_logged_users"] = f.read()

        return context
