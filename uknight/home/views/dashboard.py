import os
from django.views.generic import TemplateView
from django.conf import settings
import subprocess
import json
from systemctl.views import quick_systemctl_info

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


def total_packages_installed():
    cmd = "dpkg --list | wc -l"
    resp = subprocess.check_output(cmd, shell=True)
    return resp.decode()


def uptime():
    resp = subprocess.check_output(["uptime", "-s"]).decode("utf-8")
    return resp


def whoami():
    resp = subprocess.check_output(["whoami"]).decode("utf-8")
    return resp

def curl_ifconfig_me():
    resp = subprocess.check_output(["curl", "ifconfig.me"]).decode("utf-8")
    return resp


def last_logged_users():
    """Shows a listing (5) of last logged in users."""
    with open(os.path.join(settings.SHELL_SCRIPT_DIRS, "last.out"), "r") as f:
        users = f.read()
    return users


class DashboardView(TemplateView):
    template_name = "home/index.html"

    print(settings.SHELL_SCRIPT_DIRS)

    def get_context_data(self, *args, **kwargs):
        context = super(DashboardView, self).get_context_data(*args, **kwargs)
        context["curl_ifconfig_me"] = curl_ifconfig_me()
        context["disk_free"] = disk_free()
        context["disk_usage"] = disk_usage()
        context["free_memory_data"] = free_memory()
        context["hostnamectl"] = hostnamectl()
        context["ip_address"] = ip_address()
        context["iw_config"] = iw_config()
        context["last_logged_users"] = last_logged_users()
        context["ps"] = ps()
        context["routing_table"] = routing_table()
        context["ss"] = ss()
        context["top_services"] = quick_systemctl_info()
        context["total_installed_packages"] = total_packages_installed()
        context["uptime"] = uptime()
        context["whoami"] = whoami()
        return context
