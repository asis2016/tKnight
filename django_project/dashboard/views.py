from django.views.generic import TemplateView

#from utils.whoami import get_whoami
from utils.boottime import get_bootime
from utils.disk_partition import get_disk_partition
from utils.sensors import (
    get_sensors_temperature,
)
from utils.environ import get_environ


class DashboardTemplateView(TemplateView):
    extra_context = {'page_title': 'Dashboard'}
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['boottime'] = get_bootime()
        context['disk_partition'] = get_disk_partition()
        #context[''] =
        #context[''] =
        #context[''] =
        #context[''] =
        #context[''] =
        #context[''] =
        #context[''] =
        #context[''] =
        #context[''] =
        #context[''] =
        #context[''] =
        context['sensors_temperature'] = get_sensors_temperature()
        context['environ'] = get_environ()
        #context[''] =
        #context[''] =
        
        return context
    
    