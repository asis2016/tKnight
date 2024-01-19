from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.utils.translation import gettext as _

# utils
from utils.boottime import get_bootime
from utils.cpu import get_cpu_count
from utils.disk_partition import get_disk_partition
from utils.environ import get_environ
from utils.ifconfig import get_ifconfig
from utils.lsof import get_lsof
from utils.os_release import get_os_release
from utils.systemctl_services import get_systemctl_services
from utils.sensors import (
    get_sensors_temperature
)
from django.http import JsonResponse
from utils.users import get_users


class DashboardTemplateView(LoginRequiredMixin, TemplateView):
    extra_context = {'page_title': _('dashboard')}
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['boottime'] = get_bootime()
        context['cpu_count'] = get_cpu_count()
        context['disk_partition'] = get_disk_partition
        context['environ'] = get_environ()
        context['lsof'] = get_lsof()
        context['ifconfig'] = get_ifconfig()
        context['os_release'] = get_os_release()
        context['systemctl'] = get_systemctl_services()
        context['sensors_temperature'] = get_sensors_temperature()
        context['users'] = get_users()
        return context


class WipTemplateView(LoginRequiredMixin, TemplateView):
    extra_context = {'page_title': 'WIP'}
    template_name = 'wip.html'

def get_sensors_battery_json_view(request):
    '''
    Returns get_disk_usage() from utils as list of JSON objects.
    '''
    result = get_sensors_battery()
    return JsonResponse(result, safe=False)

def password_manager_logout(request):  
    logout(request)  
    return redirect('login')  