from django.views.generic import TemplateView

# utils
#from utils.whoami import get_whoami
from utils.boottime import get_bootime
from utils.cpu import get_cpu_count
from utils.disk_partition import get_disk_partition
from utils.environ import get_environ
from utils.ifconfig import get_ifconfig
from utils.lsof import get_lsof
from utils.os_release import get_os_release
from utils.ps import get_ps
from utils.systemctl_services import get_systemctl_services
from utils.sensors import (
    get_sensors_temperature,
)
from utils.users import get_users


class DashboardTemplateView(TemplateView):
    extra_context = {'page_title': 'Dashboard'}
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
        #context[''] =
        #context[''] =
        #context[''] =
        #context[''] =
        #context[''] =
        #context[''] =
        #context[''] =
        #context[''] =
        #context[''] =
        context['systemctl'] = get_systemctl_services()
        context['sensors_temperature'] = get_sensors_temperature()
        context['users'] = get_users()
        #context[''] =
        
        return context


